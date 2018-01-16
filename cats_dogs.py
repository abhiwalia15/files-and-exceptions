def cat_dog(filename):
	
	try:
		
		with open(filename) as f_obj:
			read = f_obj.read()
			print(read)
			
	except FileNotFoundError:
		
		print(filename + ' is missing.')
		
filenames = ['cats.txt','dogs.txt']
for filename in filenames:
	cat_dog(filename)	 

