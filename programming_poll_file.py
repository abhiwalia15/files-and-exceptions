name = input('Enter your name:')

while True:
	
	reason = input('Why do you like programming ' + name + ' ?\t')
	break
	
file_name = 'programming_poll.txt'

with open(file_name,'a') as file_object:
	
	file_object.write( '\n' + name + '\n' + reason )
