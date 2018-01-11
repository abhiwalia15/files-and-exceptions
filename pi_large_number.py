file_name = 'G:\github\eric mathews\pcc\chapter_10\pi_million_digits.txt'

with open(file_name) as file_object:
	lines = file_object.readlines()
	
pi_string = ' '

for line in lines:
	pi_string += line
	
birthday = input('input your birthday date')

if birthday in pi_string:
	print('your birthday lies in million decimal places of pi')
else:
	print('fuck you')
