import json

filename = 'username.json'

with open(filename) as f_obj:
	
	user = json.load(f_obj)
	
	print('WELCOME BACK ' + user.title() )
