
def NAND (a, b):
	if a == 1 and b == 1:
		return False
	else:
		return True


if __name__=='__main__':
	print(NAND(1, 0))

	print("+---------------+----------------+")
	print(" | NAND Truth Table | Result |")
	print(" A = False, B = False | A AND B =",NAND(False,False)," | ")
	print(" A = False, B = True | A AND B =",NAND(False,True)," | ")
	print(" A = True, B = False | A AND B =",NAND(True,False)," | ")
	print(" A = True, B = True | A AND B =",NAND(True,True)," | ")
	