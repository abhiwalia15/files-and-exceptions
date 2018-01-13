file_name = 'in_python.txt'

with open(file_name) as file_object:
	for line in file_object:
		print(line.strip().replace('python','c'))
		print(line.strip())
