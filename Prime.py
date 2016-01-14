from sys import argv

input = open(argv[1],'r')

n = 1
prime = []
for number in input:
	x=int(number)
	while x>2 and n<x:
		n +=1
		if all(n%i for i in range(2,n)):
			prime.append(n)
	
	print ",".join(map(str,prime))
	n = 1
	while len(prime)>0:
		prime.pop()
	
