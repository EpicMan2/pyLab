import random
import math
import re

# Creation of 2d matrix
def createTable(count):
	columns, rows = (count, count)
	itemslist = []
	for i in range(columns):
		col = []
		for j in range(rows):
			col.append(0)
		itemslist.append(col)
	return itemslist

# Fill with random ones
def fillTable(table):
	onesCount = len(table) * len(table)
	onesLeft = math.ceil(onesCount / 2)
	while onesLeft > 0:
		fillCol(table, len(table))
		onesLeft = onesLeft - 1
	return table

# Simple function to fill random column
def fillCol(table, count):
	x = random.randint(0, count - 1)
	y = random.randint(0, count - 1)
	currentCol = table[x][y]
	if currentCol == 1:
		fillCol(table, count)
	else:
		table[x][y] = 1

# Check verticals
def checkVertical(table):
	rowsCount = len(table[0])
	colsCount = len(table)
	matches = 0
	for i in range(colsCount):
		# Unpack a vertical
		verStr = ''
		for j in range(rowsCount):
			verStr += str(table[j][i])
		matches += checkMatch(verStr)
	return matches

# Check horizontals
def checkHorizontal(table):
	rowsCount = len(table[0])
	colsCount = len(table)
	matches = 0
	for i in range(rowsCount):
		# Unpack a horizontal
		horStr = ''
		for j in range(colsCount):
			horStr += str(table[i][j])
		matches += checkMatch(horStr)
	return matches

# Check diagonals
def checkDiagonal(table):
	rowsCount = len(table[0])
	colsCount = len(table)
	matches = 0

	for i in range(colsCount):
		j = i
		k = 0
		testStr = ''
		while k < rowsCount and j >= 0:
			testStr += str(table[j][k])
			j = j - 1
			k = k + 1
			matches += checkMatch(testStr)

	for i in range(1, rowsCount):
		j = colsCount - 1
		k = i
		testStr = ''
		while k < rowsCount and j >= 0:
			testStr += str(table[j][k])
			j = j - 1
			k = k + 1
			matches += checkMatch(testStr)
	return matches

# Check for match
def checkMatch(string):
	currLine = re.findall("([1]{4,})", string)
	if len(currLine) > 0:
		for i in range(len(currLine)):
			if len(currLine[i - 1]) == 4:
				return 1
			else:
				return 1 + (len(currLine[i]) - 4)
	else:
		return 0

print("Δώστε η διάσταση (Ένα αριθμός)")
userCount = int(input())
userMatches = 0
userInterations = 100
for x in range(userInterations):
	# Make a matrix
	userTable = createTable(userCount)
	# Fill the matrix
	formatedTable = fillTable(userTable)
	# Flip the matrix
	matrix_t = list(zip(*formatedTable))
	# Search for verticals
	userMatches += checkVertical(formatedTable)
	# Search for horizontals
	userMatches += checkHorizontal(formatedTable)
	# Search for diagonals in first matrix
	userMatches += checkDiagonal(formatedTable)
	# Search for diagonals in flipped matrix
	userMatches += checkDiagonal(matrix_t)
totalMatches = userMatches / 100
print('Επιλογή: ' + str(totalMatches))