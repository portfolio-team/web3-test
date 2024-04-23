# 1. Import Module
import json
from web3 import Web3
import config

# 2. Access Ganache local server
ganache_url = config.GANACHE_URL
web3 = Web3(Web3.HTTPProvider(ganache_url))

# 3. Account Address, private key
account_0   = config.ACCOUNT_0 # Input selected Address
account_1   = config.ACCOUNT_1 # Input selected Address
private_key = config.PRIVATE_KEY # Input selected Address's private key

# 4. Get nonce value
nonce = web3.eth.get_transaction_count(account_0)

# 5. Transaction data
tx = {
    'nonce': nonce,
    'to': account_1,
    'value': web3.to_wei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.to_wei('50', 'gwei'),
}

# 6. Generate singed transaction data
signed_tx = web3.eth.account.sign_transaction(tx, private_key)

# 7. Ethereum Transaction
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

# 8. Check Transaction address
print(Web3.to_hex(tx_hash))


