from api import Gab
import json

gab = Gab('dheerajpreddy', 'Test@123')

data = gab.get_topics(1000)

with open('topics.json', 'w') as outfile:
	json.dump(data, outfile)
