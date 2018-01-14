filename = 'alice.txt'

"""try to find a file that does not exists"""

try:
	with open(filename) as f_obj:
		print(f_obj.read())
		
except FileNotFoundError:
	print('sorry,the file ' + filename + ' does not exists.')
	
