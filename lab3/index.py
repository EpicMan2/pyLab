import requests
from datetime import datetime
import json

# Get current month
today = datetime.today()
daysCount = today.day

if today.hour > 8:
	daysCount = daysCount + 1

drawsItems = []
drawsDates = []
drawsData = {}

for i in range(1, daysCount):
	currentMonth = ''
	currentDay = ''

	if today.month < 10:
		currentMonth = '0' + str(today.month)
	else:
		currentMonth = today.month

	if i < 10:
		currentDay = '0' + str(i)
	else:
		currentDay = i

	url = "https://api.opap.gr/draws/v3.0/1100/draw-date/{}-{}-{}/{}-{}-{}/draw-id".format(today.year, currentMonth, currentDay, today.year, currentMonth, currentDay)
	request = requests.get(url)
	rtext = request.text
	rarray = json.loads(rtext)
	drawsItems.append(rarray[0])
	drawsDates.append("{}-{}-{}".format(today.year, currentMonth, currentDay))

for i in range(len(drawsItems)):
	urlDraw = "https://api.opap.gr/draws/v3.0/1100/{}".format(drawsItems[i])
	request = requests.get(urlDraw)
	rjson = request.json()
	numbersList = rjson['winningNumbers']
	drawsData[i] = numbersList

for i in range(len(drawsItems)):
	currentList = ''

	for x in range(len(drawsData[i]['list'])):
		currentList += str(drawsData[i]['list'][x]) + ' '

	currentColumns = ''
	currentColumnsJson = drawsData[i]['sidebets']['columnNumbers']

	for x in currentColumnsJson:
		currentColumns += str(currentColumnsJson[x]) + ' '

	outputStr = "Ήμερομηνία: {}\nNumbers: {}| Bonus: {}\nEven count: {}, Odd count: {}, Winning Column: {}, Winning Parity: {}\nColumn Numbers: {}".format(drawsDates[i], currentList, drawsData[i]['bonus'][0], drawsData[i]['sidebets']['evenNumbersCount'], drawsData[i]['sidebets']['oddNumbersCount'], drawsData[i]['sidebets']['winningColumn'], drawsData[i]['sidebets']['winningParity'], currentColumns)
	print(outputStr)