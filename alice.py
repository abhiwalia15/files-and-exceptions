filename = 'alice.txt'

try:
		with open(filename) as f_obj:
			contents = f_obj.read(876)
			print(contents)
		
except FileNotFoundError:
		msg = 'The file ' + filename + ' does not exist.'
		print(msg)
		
else:
		words = contents.split()
		num_words = len(words)
		print('The file '+ filename + " has "+ str(num_words) + ' words in it.')
