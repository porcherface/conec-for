
import numpy


NUM_ROW = 10
NUM_COL = 10

def valueAt(board, col, row):
	return (board >> 2 *(col + NUM_COL * row) ) % 4

def int2board(value):
	board = []
	for x in range(NUM_ROW):
		row = []
		for y in range(NUM_COL):
			val = valueAt(value, y, NUM_ROW - x - 1)
			row.append(val)
		board.append(row)	
	return board

def render(value):
	board = int2board(value)
	print("  V  V  V  V  V  V  V  V  V  V  ")
	for row in board:
		rowstring = "|"
		for val in row:
			if val == 0:
				rowstring += "   "
			if val == 1:
				rowstring += " O "
			if val == 2:
				rowstring += " X "
			if val == 3:
				raise ValueError	
		rowstring += "|"
		print(rowstring)

if __name__ == "__main__":

	print("hello test!")

	render(0)
	print()
	render(1)
	print()
	render(9)
	print()
	render(1048585)