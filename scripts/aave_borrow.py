from brownie import network, config, interface
from scripts.get_weth import get_weth
from scripts.helpful_scripts import get_account
from web3 import Web3

amount = Web3.toWei(0.1, "ether")


def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    if network.show_active() in ["mainnet-fork"]:
        get_weth()
    # when we need a contract we need: abi, address
    lending_pool = get_lending_pool()
    # approve sending out our erc20 tokens
    approve_erc20(amount, lending_pool.address, erc20_address, account)
    print("Depositing...")
    txn = lending_pool.deposit(erc20_address, amount, account.address, 0, {"from": account})
    txn.wait(1)
    print("Deposited")


def approve_erc20(amount, spender, erc20_address, account):
    print("Approving ERC20 token...")
    # need abi, address to call approve function for erc20
    erc20 = interface.IERC20(erc20_address)
    txn = erc20.approve(spender, amount, {"from": account})
    txn.wait(1)
    print("Approved")
    return txn


def get_lending_pool():
    lending_pool_addresses_provider = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"]
    )
    lending_pool_address = lending_pool_addresses_provider.getLendingPool()
    # need abi, address
    lending_pool = interface.ILendingPool(lending_pool_address)
    return lending_pool
