name = input('Enter your name:')

while name:
	
	msg = 'WELCOME,' + name
	print(msg)
	break
	
file_name = 'guest_book.txt'

with open(file_name,'a') as file_object:
	
	file_object.write('\n'+msg)

