import json

num = int(input('Enter your favourite number'))

filename = 'fav_num.json'

with open(filename,'w') as f_obj:
	
	json.dump(num,f_obj)
	
