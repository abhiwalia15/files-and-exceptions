name = input('Enter your name')

filename = 'name.txt'

with open(filename,'a') as file_object:
	
	file_object.write('\n'+name)
	
