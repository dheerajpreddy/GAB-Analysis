import collections
import re
import json
from nltk.corpus import stopwords


def tokenize(string):
    """Convert string to lowercase and split into words (ignoring
    punctuation), returning list of words.
    """
    return re.findall(r'\w+', string.lower())


def count_ngrams(lines, min_length=2, max_length=3):
    """Iterate through given lines iterator (file object or list of
    lines) and return n-gram frequencies. The return value is a dict
    mapping the length of the n-gram to a collections.Counter
    object of n-gram tuple and number of times that n-gram occurred.
    Returned dict includes n-grams of length min_length to max_length.
    """
    lengths = range(min_length, max_length + 1)
    ngrams = {length: collections.Counter() for length in lengths}
    queue = collections.deque(maxlen=max_length)

    # Helper function to add n-grams at start of current queue to dict
    def add_queue():
        current = tuple(queue)
        for length in lengths:
            if len(current) >= length:
                ngrams[length][current[:length]] += 1

    # Loop through all lines and words and add n-grams to dict
    # for line in lines:
    for word in tokenize(lines):
        queue.append(word)
        if len(queue) >= max_length:
            add_queue()

    # Make sure we get the n-grams at the tail end of the queue
    while len(queue) > min_length:
        queue.popleft()
        add_queue()

    return ngrams


def print_most_frequent(ngrams, num=10):
    """Print num most common n-grams of each length in n-grams dict."""
    for n in sorted(ngrams):
        print('----- {} most common {}-grams -----'.format(num, n))
        for gram, count in ngrams[n].most_common(num):
            print('{0}: {1}'.format(' '.join(gram), count))
        print('')

cachedStopWords = stopwords.words("english")

def removeStopWords(text):
        text = ' '.join([word for word in text.split() if word not in cachedStopWords])
        return text

if __name__ == '__main__':

    with open('hates999.json', 'r') as fp:
        responses = json.load(fp)
    fp.close()
    hate_str = ""
    offense_str = ""
    neither_str = ""
    for i in range(len(responses)):
        if responses[i]['top_class'] == "hate_speech":
            hate_str = hate_str + responses[i]['text']
        elif responses[i]['top_class'] == "offensive_language":
            offense_str = offense_str + responses[i]['text']
        else:
            neither_str = neither_str + responses[i]['text']
    hate_str = re.sub(r"http\S+", "", hate_str)
    offense_str = re.sub(r"http\S+", "", offense_str)
    neither_str = re.sub(r"http\S+", "", neither_str)
    hate_str = removeStopWords(hate_str)
    offense_str = removeStopWords(offense_str)
    neither_str = removeStopWords(neither_str)
    ngrams = count_ngrams(hate_str)
    print_most_frequent(ngrams)

    ngrams = count_ngrams(offense_str)
    print_most_frequent(ngrams)

    ngrams = count_ngrams(neither_str)
    print_most_frequent(ngrams)
