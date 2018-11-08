from api import Gab
import json

gab = Gab('dheerajpreddy', 'Test@123')

data = gab.get_trending_gabs(10000)

print (len(data))

with open('trending_gabs.json', 'w') as outfile:
	json.dump(data, outfile)
