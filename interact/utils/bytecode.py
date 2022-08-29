#bytecode.py
import json

PATH_TRUFFLE_WK = '/Users/saramilone/ricciobbello/conec-for'


def getBytecode(contract_name):
	
	return json.load(open(PATH_TRUFFLE_WK + '/build/contracts/'+contract_name+'.json'))['bytecode']

if __name__ == "__main__":
	
	c=getBytecode("Caos")
	f=getBytecode("Factory")
	a=getBytecode("Faucet")
	b=getBytecode("Butterfly")
	
	with open("Caos", 'w') as x: x.write(c)
	x.close()
	with open("Factory", 'w') as x: x.write(f)
	x.close()
	with open("Faucet", 'w') as x: x.write(a)
	x.close()
	with open("Butterfly", 'w') as x: x.write(b)
	x.close()
	