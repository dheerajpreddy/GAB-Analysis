from api import Gab
import json

gab = Gab('dheerajpreddy', 'Test@123')

with open('username.json', 'r') as fp:
    people = json.load(fp)
fp.close()
all_gabs = []

for i in range(len(people)):
    print(i, len(all_gabs))
    if people[i]['is_private'] is False:
        try:
            gabs = gab.getusertimeline(people[i]['username'])['data']
            all_gabs = all_gabs + gabs
        except:
            print("ERROR for " + people[i]['username'])

fp2 = open('gabs999.json', 'w')
json.dump(all_gabs, fp2)
fp2.close()
