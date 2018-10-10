import json

with open('hates999.json', 'r') as fp:
    responses = json.load(fp)
fp.close()

hate = 0
offensive = 0
neither = 0

for i in range(len(responses)):
    if responses[i]['top_class'] == "hate_speech":
        hate += 1
    elif responses[i]['top_class'] == "offensive_language":
        offensive += 1
    else:
        neither +=1

print("Hate #: ", hate*100/float(len(responses)))
print("Offensive #: ", offensive*100/float(len(responses)))
print("Neither #: ", neither*100/float(len(responses)))

print(len(responses))
