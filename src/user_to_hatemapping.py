from api import Gab
import json
from hatesonar import Sonar

sonar = Sonar()
gab = Gab('dheerajpreddy', 'Test@123')

with open('username.json', 'r') as fp:
	people = json.load(fp)
fp.close()

for i in range(len(people)):
	flg1 = 0
	flg2 = 0
	flg = 0
	if people[i]['is_private'] is False:
		try:
			gabs = gab.getusertimeline(people[i]['username'], 100)
		except:
			flg = 1
			print("ERROR for " + people[i]['username'])
		if flg:
			continue
		for data in gabs:
			response = sonar.ping(text=data['post']['body'])
			if response['top_class'] == 'hate_speech':
				flg1 = 1
			if response['top_class'] == 'offensive_language':
				flg2 = 1
		if flg1:
			people[i]['is_hate_speech'] = True
		if flg2:
			people[i]['is_offensive_language'] = True
		if flg1==0 and flg2==0:
			people[i]['is_neutral'] = True
	else:
		print (people[i]['username'])
	print (i)

with open('users_with_labels.json', 'w') as outfile:
	json.dump(people, outfile)
