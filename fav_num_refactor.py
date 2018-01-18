import json

def read_fav_num():
	try:
		filename = 'fav_num.json'

		with open(filename)as f_obj:
	
			my_num = json.load(f_obj)
	
			
		
	except FileNotFoundError:
		
		num = int(input('Enter your favourite number'))

		filename = 'fav_num.json'

		with open(filename,'w') as f_obj:
		
			json.dump(num,f_obj)
			
	else:
		
		print('I know your favourite number is ' + str(my_num))
		
read_fav_num()


		
		
	
