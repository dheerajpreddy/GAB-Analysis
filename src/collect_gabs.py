from api import Gab
import json

gab = Gab('dheerajpreddy', 'Test@123')

with open('username.json', 'r') as fp:
    people = json.load(fp)
fp.close()

with open("gabs999.json", 'w') as f:
    json.dump([], f)

for i in range(2000):
    with open('gabs999.json') as f2:
        json_data = json.load(f2)
    print(i, len(json_data))
    if people[i]['is_private'] is False:
        try:
            gabs = gab.getusertimeline(people[i]['username'])['data']
            json_data = json_data + gabs
            with open("gabs999.json", 'w') as feedsjson:
                json.dump(json_data, feedsjson)
        except:
            print("ERROR for " + people[i]['username'])
