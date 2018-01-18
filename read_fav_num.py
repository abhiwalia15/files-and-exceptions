import json

filename = 'fav_num.json'

with open(filename)as f_obj:
	
	my_num = json.load(f_obj)
	
	print('I know your favourite number is ' + str(my_num))
