from sys import argv

input = open(argv[1],'r')#extract input line-by-line

numbers=[]
for integer in input:#add all integers to a list
	numbers.append(int(integer))
	
sum = 0
while len(numbers)>0:
	sum = sum + numbers.pop()
	
print sum
