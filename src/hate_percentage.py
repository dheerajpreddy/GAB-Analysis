import json
import matplotlib.pyplot as plt

with open('case_study_sonar.json', 'r') as fp:
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
h = hate*100/float(len(responses))
o = offensive*100/float(len(responses))
n = neither*100/float(len(responses))

# print("Hate #: ", hate*100/float(len(responses)))
# print("Offensive #: ", offensive*100/float(len(responses)))
# print("Neither #: ", neither*100/float(len(responses)))

# print(len(responses))
# Data to plot
labels = ['Hate', 'Offensive', 'Neither']
sizes = [h, o, n]
colors = ['red', 'gold', 'yellowgreen']
explode = (0.2, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
