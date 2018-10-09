from hatesonar import Sonar
import json
import re
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk
from wordcloud import WordCloud

fp = open('hates999.json', 'r')
responses = json.load(fp)
fp.close()

stop_words = list(stopwords.words('english'))
for i in range(0, len(stop_words)):
	stop_words[i] = stop_words[i].lower()

for response in responses:
	text = response['text']
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
fig1.savefig('wordcloud_neutral_gabs.png')

fig2 = plt.figure(figsize=(25, 15))
plt.imshow(wordcloud_offensive)
plt.axis("off")
plt.tight_layout(pad = 0)
fig2.savefig('wordcloud_offensive_gabs.png')

fig3 = plt.figure(figsize=(25, 15))
plt.imshow(wordcloud_hate)
plt.axis("off")
plt.tight_layout(pad = 0)
fig3.savefig('wordcloud_hate_gabs.png')

offensive_word_list = offensive_text.split()
hate_word_list = hate_text.split()
offensive_text = ''
hate_text = ''

fp2 = open('word_mapping999.json', 'r')
word_mapping = json.load(fp2)
fp2.close()

for word in offensive_word_list:
	if word in word_mapping:
		if word_mapping[word] == 'offensive_language':
			offensive_text = offensive_text + ' ' + word

for word in hate_word_list:
	if word in word_mapping:
		if word_mapping[word] == 'hate_speech':
			hate_text = hate_text + ' ' + word

wordcloud_offensive_words = WordCloud(width = 800, height = 800, background_color ='white', min_font_size = 10).generate(offensive_text)
wordcloud_hate_words = WordCloud(width = 800, height = 800, background_color ='white', min_font_size = 10).generate(hate_text)

fig4 = plt.figure(figsize=(15, 10))
plt.imshow(wordcloud_offensive_words)
plt.axis("off")
plt.tight_layout(pad = 0)
fig4.savefig('wordcloud_offensive_words.png')

fig5 = plt.figure(figsize=(15, 10))
plt.imshow(wordcloud_hate_words)
plt.axis("off")
plt.tight_layout(pad = 0)
fig5.savefig('wordcloud_hate_words.png')
