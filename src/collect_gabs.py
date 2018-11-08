from api import Gab
import json

gab = Gab('dheerajpreddy', 'Test@123')

with open('username.json', 'r') as fp:
    people = json.load(fp)
fp.close()

total = 50000
count = 0
haha = 0

with open('newgabs.json', 'w') as f:
	json.dump([], f)
f.close()

for user in people:
	print (haha)
	print (count)
	print ('\n')
	if count >= total:
		break
	haha += 1
	print (user)
	try:
		with open('newgabs.json', 'r') as fp:
			data = json.load(fp)
		fp.close()
		username = user['username']
		gabs = gab.getusertimeline(username, 100)
		count += len(gabs)
		data += gabs
		with open('newgabs.json', 'w') as f:
			json.dump(data, f)
		f.close()
	except:
		continue
