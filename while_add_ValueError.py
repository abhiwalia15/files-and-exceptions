try:
	
	print('enter any two numbers to add')
	print('enter q to exit')
	
	while True:
		n = int(input('first -'))
		m = int(input('second -'))
		sum = n + m
		print(sum)
		
except ValueError:
	print('This in not an integer')
