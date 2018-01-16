filename = 'alice.txt'

with open(filename) as f_obj:
	 contents = f_obj.read()
	 count = contents.count('the')
	 print(count)
	 
