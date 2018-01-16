def count_num(filename):
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFountError:
		pass
	else:
		count_num = contents.split()
		print(filename + ' - ' + str(len(count_num)))
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_num(filename)
