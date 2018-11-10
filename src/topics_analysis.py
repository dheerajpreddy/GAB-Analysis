import json
import re
from nltk.corpus import stopwords
from hatesonar import Sonar
from wordcloud import WordCloud
import nltk
import matplotlib.pyplot as plt

fp = open('trending_gabs.json', 'r')
gabs = json.load(fp)
fp.close()

sonar = Sonar()

stop_words = list(stopwords.words('english'))
for i in range(0, len(stop_words)):
	stop_words[i] = stop_words[i].lower()

hate = 0
offensive = 0
neutral = 0
hate_text = ''
offensive_text = ''
neutral_text = ''

for i in range(360, len(gabs)):
	text = gabs[i]['post']['body']
	text = re.sub(r"http\S+", "", text)
	word_list = re.sub("[^\w]", " ", text).split()
	words_to_remove = []

	for i in range(0, len(word_list)):
		word_list[i] = word_list[i].lower()

	for word in word_list:
		if word in stop_words:
			words_to_remove.append(word)

	for word_to_remove in words_to_remove:
		if word_to_remove in word_list:
			word_list.remove(word_to_remove)

	new_text = ''
	for word in word_list:
		new_text = new_text + word + ' '

	gabs[i]['post']['body'] = new_text

	response = sonar.ping(text=new_text)

	if response['top_class'] == 'hate_speech':
		hate += 1
		hate_text = hate_text + ' ' + text

	if response['top_class'] == 'offensive_language':
		offensive += 1
		offensive_text = offensive_text + ' ' + text

	if response['top_class'] == 'neither':
		neutral += 1
		neutral_text = neutral_text + ' ' + text

wordcloud_offensive = WordCloud(width = 800, height = 800, background_color ='white', stopwords = stop_words, min_font_size = 10).generate(offensive_text)
wordcloud_hate = WordCloud(width = 800, height = 800, background_color ='white', stopwords = stop_words, min_font_size = 10).generate(hate_text)
wordcloud_neutral = WordCloud(width = 800, height = 800, background_color ='white', stopwords = stop_words, min_font_size = 10).generate(neutral_text)

fig1 = plt.figure(figsize=(25, 15))
plt.imshow(wordcloud_offensive)
plt.axis("off")
plt.tight_layout(pad = 0)
fig1.savefig('wordcloud_offensive_trending_gabs.png')

fig2 = plt.figure(figsize=(25, 15))
plt.imshow(wordcloud_hate)
plt.axis("off")
plt.tight_layout(pad = 0)
fig2.savefig('wordcloud_hate_trending_gabs.png')

fig3 = plt.figure(figsize=(25, 15))
plt.imshow(wordcloud_neutral)
plt.axis("off")
plt.tight_layout(pad = 0)
fig3.savefig('wordcloud_neutral_trending_gabs.png')

labels = 'Neutral', 'Offensive', 'Hate'
sizes = [neutral, offensive, hate]
colors = ['green', 'red', 'black']
explode = (0.1, 0, 0)
 
fig3 = plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.show()
