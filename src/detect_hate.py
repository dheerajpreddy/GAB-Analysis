from hatesonar import Sonar
import json

sonar = Sonar()

with open('gabs.json', 'r') as fp:
    gabs = json.load(fp)
fp.close()

responses =[]

for i in range(len(gabs)):
    responses.append(sonar.ping(text=gabs[i]['post']['body']))

fp2 = open('hates.json', 'w')
json.dump(responses, fp2)
fp2.close()
