import json

def get_stored_user():
	'''get stored username if available'''
	filename='username.json'
	try:
		with open(filename)as f_obj:
			name=json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return name

def get_new_user():
	username=input('Enter your name?')
	filename='username.json'
	with open(filename,'w')as f_obj:
		json.dump(username,f_obj)
	return username
	
def greet_user():
	'''Now greet the user by name'''
	username=get_stored_user()
	if username:
		print('WELCOME BACK '+username)
		
	else:
		username=get_new_user()
		print('WE WILL REMEMBER YOU WHEN YOU COME BACK '+username)
		
greet_user()
