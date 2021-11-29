
from brownie import network, interface, config
from scripts.helpful_scripts import get_account


def main():
    get_weth()

def get_weth():
    """
    Mints WETH by depositing ETH.
    """
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    txn = weth.deposit({"from": account, "value": 0.1 * 10 **18})
    txn.wait(1)
    print(f"Received 0.1 WETH")