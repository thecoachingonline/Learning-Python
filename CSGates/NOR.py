
def NOR(a, b):
	if(a == 0) and (b == 0):
		return 1
	elif(a == 0) and (b == 1):
		return 0
	elif(a == 1) and (b == 0):
		return 0
	elif(a == 1) and (b == 1):
		return 0


if __name__=='__main__':
	print(NOR(0, 0))

	print("+---------------+----------------+")
	print(" | NOR Truth Table | Result |")
	print(" A = False, B = False | A NOR B =",NOR(False,False)," | ")
	print(" A = False, B = True | A NOR B =",NOR(False,True)," | ")
	print(" A = True, B = False | A NOR B =",NOR(True,False)," | ")
	print(" A = True, B = True | A NOR B =",NOR(True,True)," | ")
