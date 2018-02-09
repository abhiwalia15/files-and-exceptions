filename = 'cats.txt'

with open(filename) as f:
	contents = f.readlines()
	
print(contents.split(','))
