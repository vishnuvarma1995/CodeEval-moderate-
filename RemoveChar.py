from sys import argv



def RemoveChar(line):
	for letters in line[1]:
		line[0] = line[0].replace(letters,"")
	return line[0]
	
def main():
	with open(argv[1],'r') as input:
		for line in input:
			if len(line) > 1:
				line = line.strip().split(',')
				
				line[1] = line[1].strip()
				print RemoveChar(line)

main()
