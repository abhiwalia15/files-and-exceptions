def num_count(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
		
	except FileNotFoundError:
		msg = 'The file ' + filename + ' does not exist.'
		print(msg)
		
	else:
		words = contents.split()
		num_words = len(words)
		print('The file '+ filename + " has "+ str(num_words) + ' words in it.')

filename = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filenames in filename:
	num_count(filenames)
