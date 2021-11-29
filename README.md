# Aave brownie
1. Swap our ETH for WETH
2. Deposit some ETH into Aave
3. Borrow some asset with the ETH collateral
    1. Sell that borrowed asset. (short selling)
4. Repay everything

## Testing

### Integration test: Kovan
### Unit tests: Mainnet-fork (bc no oracles, if not we would use development with mocking)