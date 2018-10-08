from hatesonar import Sonar
import json
import re
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk
from wordcloud import WordCloud

fp = open('hates.json', 'r')
responses = json.load(fp)
fp.close()

for response in responses:
	text = response['text']
	text = re.sub(r"http\S+", "", text)
	word_list = re.sub("[^\w]", " ", text).split()
	stop_words = list(stopwords.words('english'))
	words_to_remove = []
	
	for word in word_list:
		word = word.lower()
		if word in stop_words:
			words_to_remove.append(word)

	for word_to_remove in words_to_remove:
		if word_to_remove in word_list:
			word_list.remove(word_to_remove)

	new_text = ''
	for word in word_list:
		new_text = new_text + word + ' '

	response['text'] = new_text

neutral_text = ''
hate_text = ''
offensive_text = ''

for response in responses:
	text = response['text']
	if response['top_class'] == 'neither':
		neutral_text = neutral_text + ' ' + text
	if response['top_class'] == 'hate_speech':
		hate_text = hate_text + ' ' + text
	if response['top_class'] == 'offensive_language':
		offensive_text = offensive_text + ' ' + text

wordcloud_neutral = WordCloud(width = 800, height = 800, background_color ='white', stopwords = stop_words, min_font_size = 10).generate(neutral_text)
wordcloud_offensive = WordCloud(width = 800, height = 800, background_color ='white', stopwords = stop_words, min_font_size = 10).generate(offensive_text)
wordcloud_hate = WordCloud(width = 800, height = 800, background_color ='white', stopwords = stop_words, min_font_size = 10).generate(hate_text)
fig1 = plt.figure(figsize=(25, 15))
plt.imshow(wordcloud_neutral)
plt.axis("off")
plt.tight_layout(pad = 0)
fig1.savefig('neutral_wordcloud.png')
fig2 = plt.figure(figsize=(25, 15))
plt.imshow(wordcloud_offensive)
plt.axis("off")
plt.tight_layout(pad = 0)
fig2.savefig('offensive_wordcloud.png')
fig3 = plt.figure(figsize=(25, 15))
plt.imshow(wordcloud_hate)
plt.axis("off")
plt.tight_layout(pad = 0)
fig3.savefig('hate_wordcloud.png')
