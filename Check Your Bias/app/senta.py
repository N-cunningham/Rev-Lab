import csv
import nltk
from nltk import FreqDist
import json
from os import listdir
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
additional_stopords = [":", "RT", "'", "'s", "The", "-", "?", ",", '"', '”', '“', "'", "'", "'", "'", "$", ")", "(", "_", "&", '...', '.', '�', ';', '!', "''", "``", "%", "@", "--", ".", "[", "]", "[]", "[ ]", "’", "|", "‘", "'", ".", " ", "e", "i", "a", "r", "."]

tweets = []
retweets = []
column = 7
seperator = " "

with open('C:/Users/Niall/Documents/GitHub/Rev-Lab/senta/data/tweets.csv', encoding="utf8") as f:
  data = csv.reader(f)
  for row in data:
      if len(row[column]) > 2:
          start = str(row[column][0]) + str(row[column][1])
          if start == "RT":
            retweets.append(row[column])
          else:
              tweets.append(row[column])

tweets = seperator.join(tweets)
tweetsWordsRaw = word_tokenize(tweets)
tweetsWords = []
for word in tweetsWordsRaw:
    if word not in additional_stopords:
         tweetsWords.append(word)
tweetsFreqDist = FreqDist(tweetsWords)

retweets = seperator.join(retweets)
retweetsWordsRaw = word_tokenize(retweets)
retweetsWords = []
for word in retweetsWordsRaw:
    if word not in additional_stopords:
         retweetsWords.append(word)
retweetsFreqDist = FreqDist(retweetsWords)


print(tweetsFreqDist)
print(tweetsFreqDist.most_common(15))

print(retweetsFreqDist)
print(retweetsFreqDist.most_common(15))
