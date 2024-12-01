input = '''LONG INPUT STRING'''
listOne = []
listTwo = []
sumOfDifferences = 0
for listItem in input.split('\n'):
	listItemOne,listItemTwo = listItem.split('   ')
	listOne.append(int(listItemOne))
	listTwo.append(int(listItemTwo))
listOne.sort()
listTwo.sort()
i=0
n=len(listOne)
while(i<n):
	if(listOne[i]>listTwo[i]):
		sumOfDifferences = sumOfDifferences + listOne[i] - listTwo[i]
	else:
		sumOfDifferences = sumOfDifferences + listTwo[i] - listOne[i]
	i = i+1
print(sumOfDifferences)