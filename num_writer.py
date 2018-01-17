import json

nums = [2,3,4,5,6,7,14,15,16]

filename = 'nums.json'

with open(filename,'w') as f_obj:
	
	json.dump(nums,f_obj)
