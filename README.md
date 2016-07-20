# Auto-Summarization
Provides an auto summary of a given article.

Techniques so far:

  - Scoring words based upon frequency and then using sentences with the most frequent words (extremely simplistic and doesn't work very well)
  - TFIDF Score based vector representation of sentences, then comparing the sums of each sentence's score and choosing the highest scoring sentences (also very simplistic, but works a little better)
