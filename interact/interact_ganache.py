# interact_ganache.py
import web3
import json
from utils.abi import getAbi
from render.int2board import render
# this script makes python interact with the ganache local blockchain

w3 = web3.Web3(web3.HTTPProvider('http://127.0.0.1:7545'))


print(w3.clientVersion)


player1_addr           = "0xB55F9EfFa5147372177050AcFff53535d581bEd1"
player1_private_key    = "8a85819e092d0bc8b38c76cdbc7e7ed7ef23e69f37e0e7bdbd5c9431f5b9a6b7"
player2_addr           = "0xb133ED4008CAE1fbc9AD0E7210d403eBec1bdC16"
player2_private_key    = "6b292a34b8c2d9517eda1ff2bfc3e56c51828715cb74f10c05b897f98906a5c9"
game_addr              = "0xb8A21eA49a53730186849c37d9c684522C940cFf"

w3.eth.default_account = player1_addr
print(w3.eth.default_account)

if __name__ == "__main__":
	
	game = w3.eth.contract(address = game_addr, abi = getAbi("ConecGame"))
	ans = "x"
	
	while ans != "q" and ans != None:

		if ans == "b":	
			board = game.functions.getBoard().call()
			print("BOARD:")
			render(board)



		ans = input("what u want to do?")


