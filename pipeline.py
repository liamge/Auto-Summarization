from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk import FreqDist
from operator import itemgetter
import urllib.request, re
from bs4 import BeautifulSoup
from stop_list import closed_class_stop_words


article = urllib.request.urlopen(input('Input URL here:')).read()
soup = BeautifulSoup(article, 'html.parser')
text = str(soup.find_all('p'))
cleaned_article = re.sub(r'<.*?>,?', '', text)
cleaned_article = cleaned_article[1:len(cleaned_article)-1]
cleaned_article = re.sub(r'\[.*?\]', '', cleaned_article)

sentences = sent_tokenize(cleaned_article)
words = word_tokenize(cleaned_article)

# Strip stop words
words = [word for word in words if word not in closed_class_stop_words]

# Stemming
stemmer = SnowballStemmer("english")
stemmed_words = [stemmer.stem(word) for word in words]

# FDist
fdist = FreqDist(stemmed_words)

# Placeholder solution to get pipeline up and running
def score_sents(sentences):
    scores = []
    for (i, sent) in enumerate(sentences):
        score = []
        for word in sent:
            score.append(fdist[word])
        scores.append((i, sum(score)))
    return sorted(scores, reverse=True, key=itemgetter(1))

def main(number_of_sents):
    scores = score_sents(sentences)[:number_of_sents]
    final = '\n'.join(sentences[i] for (i, score) in scores)
    print(final)
    print('Reduced total article by %d percent' % (100-(100*(number_of_sents/len(sentences)))))

main(int(input('How many sentences:')))