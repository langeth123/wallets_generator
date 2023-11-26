from eth_account import Account

WALLETS = 1000

secrets, addresses = [], []
for _ in range(WALLETS):
    web_account = Account.create()
    secrets.append(web_account.key.hex())
    addresses.append(web_account.address)

with open("secrets.txt", 'w') as file:
    for i in secrets: file.write(i + '\n')

with open("addresses.txt", 'w') as file:
    for i in addresses: file.write(i + '\n')