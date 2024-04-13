from web3 import Web3

# Web3オブジェクトの生成
w3 = Web3()

# 新しいアカウントの生成
new_account = w3.eth.account.create()

# 秘密鍵とアドレスの出力
print("Address:", new_account.address)
print("Private Key:", new_account.key.hex())
