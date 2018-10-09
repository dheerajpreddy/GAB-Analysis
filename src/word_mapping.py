from hatesonar import Sonar
import json
import re
import nltk
from nltk.corpus import stopwords

sonar = Sonar()

with open('gabs999.json', 'r') as fp:
	gabs = json.load(fp)
fp.close()

text = ''
for gab in gabs:
	text = text + gab['post']['body']

text = re.sub(r"http\S+", "", text)
word_list = re.sub("[^\w]", " ", text).split()
stop_words = list(stopwords.words('english'))
words_to_remove = []

for i in range(0, len(word_list)):
	word_list[i] = word_list[i].lower()

for word in word_list:
	if word in stop_words:
		words_to_remove.append(word)

for word_to_remove in words_to_remove:
	if word_to_remove in word_list:
		word_list.remove(word_to_remove)

word_mapping = dict()

for word in word_list:
	if word not in word_mapping:
		response = sonar.ping(text=word)
		word_mapping[word] = response['top_class']

fp2 = open('word_mapping999.json', 'w')
json.dump(word_mapping, fp2)
fp2.close()
