import copy

#------- introductory examples ----------
#recursion example 1: fibonacci #s
def fib(n):
	if n==1 or n==0:
		return 1 #terminate the recursion for the first two terms
	else:
		return fib(n-1)+fib(n-2) #otherwise branch out



#using recursion to evaluate expressions
def check(x, y, z):
	return (x+y+z)*(x+y+z) == x*x + y*y + z*z

#making an n-dimensional loop
def loop(args, n, layercount, limit, argslist):
	# if the loop has reached the nth layer, run a normal loop
	if layercount == n-1:
		for i in range(limit):
			args[layercount]=i
			argslist.append(copy.deepcopy(args))
		return argslist
			# print "the theorem is "+str(check(args[0], args[1], args[2])) + " for the values "+str(args)
	# if the loop has more layers to go, start a new loop
	else:
		for i in range(limit):
			args[layercount]=i
			argslist = loop(args, n, layercount+1, limit, argslist)
		return argslist

#-------------------------------
# -1 represents an unset value, anything non-negative is preset
# sudokugame = [[-1, 2, 0],[1, -1, -1],[-1, -1, -1]] #this game has no solution
sudokugame = [[-1, 2, 0],[2, -1, -1],[-1, -1, -1]] #this game has a solution

def checkError(game, position):
	# position: (row, column)
	# for each item in the same row and same column, check for similarity
	for col in range(3):
		if game[position[0]][col] == game[position[0]][position[1]] and col != position[1]:
			return False
	for row in range(3):
		if game[row][position[1]] == game[position[0]][position[1]] and row != position[0]:
			return False
	return True

#check the entire game
def checkGame(game):
	for col in range(3):
		for row in range(3):
			if not checkError(game, (row, col)):
				return False
	return True

#add all unset values to a list
unsetvalues = []
for i in range(len(sudokugame)):
	for j in range(len(sudokugame)):
		if sudokugame[i][j]==-1:
			unsetvalues.append((i, j))

#initialize a null array of correct right length
args = [0 for i in range(len(unsetvalues))]

#get out configurations vector using the n-dimensional loop
configurations = loop(args, len(unsetvalues), 0, 3, [])

def findCorrectGame():
	for configuration in configurations:
		newgame = copy.deepcopy(sudokugame)
		for i in range(len(unsetvalues)):
			value = unsetvalues[i]
			newgame[value[0]][value[1]] = configuration[i]
		if checkGame(newgame):
				return newgame


print findCorrectGame()