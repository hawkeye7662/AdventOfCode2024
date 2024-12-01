input = '''LONG INPUT STRING'''
listOne = []
listTwo = []
for listItem in input.split('\n'):
	listItemOne,listItemTwo = listItem.split('   ')
	listOne.append(int(listItemOne))
	listTwo.append(int(listItemTwo))
from collections import Counter
listTwoMap = Counter(listTwo)
secondAnswer = 0
for item in listOne:
	if item in listTwoMap:
		secondAnswer = secondAnswer + listTwoMap[item]*item
print(secondAnswer)
