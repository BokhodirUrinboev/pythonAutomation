import random 

def random_number():
	return random.randint(1, 100)


def create_file():
	f = open('inputFile.txt','r')
	# print(f.read())
	w = open('CreateFile.txt', 'w')

	for line in f:
		score = random_number()
		if score > 55:
			w.writelines(line.rstrip() + "  "+ str(score)+"  Pass\n")
		else:
			w.writelines(line.rstrip() + "  "+ str(score)+"  Fail\n")	
	f.close()
	w.close()


def read_file():
	f = open('CreateFile.txt','r')
	# print(f.read())

	for line in f:
		line_split = line.split()
		if line_split[2] == "Pass":
			print(line)
	f.close()

# read_file()	

# create_file()
