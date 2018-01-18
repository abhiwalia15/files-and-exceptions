import json 

filename = 'username.json'

try:
	with open(filename)as f_obj:
		user = json.load(f_obj)
		
except FileNotFoundError:
	username = input('Enter your name?')
	with open(filename,'w')as f_obj:
		json.dump(username,f_obj)
		print('We\'ll remember you ' + username.title())
		
else:
	print('WELCOME BACK ' + user.title())
