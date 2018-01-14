print('Enter any two numbers to divide')
print('Enter q to quit')

while True:
	
	n = input('first number:')
	if n == 'q':
		break
		
	m = input('second number:')
	if m == 'q':
		break
	
	try:
		answer = int(n)/int(m)
		
	except ZeroDivisionError:
		print('You cant divide this')
		
	else:
		print(answer)
