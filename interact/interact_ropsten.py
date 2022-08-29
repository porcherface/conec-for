# interact_ganache.py
import web3
import json
from utils.abi import getAbi
from utils.private import getPrivate

try:
	import utils.accounts
except:
	print("accounts.py not found, skipping")

# this script makes python interact with the ropsten public blockchain
# using infura provider
w3 = web3.Web3(web3.HTTPProvider('https://ropsten.infura.io/v3/9b60a47c62674390b98e45168938a5fc'))


print(w3.clientVersion)

w3.eth.default_account = w3.eth.account.privateKeyToAccount(getPrivate())
default_address = str(w3.eth.default_account.address)

print(w3.eth.default_account)
print(default_address)

transact_params = {
    'from': default_address,
    'gas': 21000,
    'gas_price': 1,
}


game_addr = None
if __name__ == "__main__":
	
	print("Tring to connect to game @:"+game_addr)
	game = w3.eth.contract(address = game_addr, abi = getAbi("ConecGame"))
	print("done")
	ans = "x"
		
	while ans != "q" and ans != None:

		if ans == "b":	
			board = game.functions.getBoard().call()
			print("BOARD:")
			render(board)



		ans = input("what u want to do?")

