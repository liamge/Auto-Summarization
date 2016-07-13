from nltk.tokenize import sent_tokenize, word_tokenize
from operator import itemgetter
import urllib.request, re
from bs4 import BeautifulSoup


article = urllib.request.urlopen(input('Input URL here:')).read()
soup = BeautifulSoup(article, 'html.parser')
text = str(soup.find_all('p'))
cleaned_article = re.sub(r'<.*?>,?', '', text)
cleaned_article = cleaned_article[1:len(cleaned_article)-1]
cleaned_article = re.sub(r'\[.*?\]', '', cleaned_article)

sentences = sent_tokenize(cleaned_article)
tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]

# Using the set of sentences S we can use tf of term in sentence multiplied by idf of term in S
# For TFIDF score, then sum all scores for sentence score
from math import log

def tf(t, d):
    count = 0
    for word in d:
        if word == t:
            count += 1
    return count

def idf(t, D):
    docs_containing_term = 0
    for doc in D:
        if t in doc:
            docs_containing_term += 1
    # Equation plus adding 1 in the denominator to prevent divide by zero error
    return log((len(D) / (1 + docs_containing_term)))

def tfidf(t, d, D):
    return tf(t, d) * idf(t, D)


# Placeholder solution to get pipeline up and running
def score_sents(sentences):
    all_scores = []
    for (i, sentence) in enumerate(sentences):
        sentence_score = []
        for word in sentence:
            sentence_score.append(tfidf(word, sentence, sentences))
        all_scores.append((i, sum(sentence_score)))
    return sorted(all_scores, key=itemgetter(1), reverse=True)

def main(number_of_sents):
    scores = score_sents(tokenized_sentences)[:number_of_sents]
    final = '\n'.join(sentences[i] for (i, score) in scores)
    print(final)
    print('Reduced total article by %d percent' % (100-(100*(number_of_sents/len(sentences)))))

main(int(input('How many sentences:')))