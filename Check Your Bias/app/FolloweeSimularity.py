#cosine simularity of your tweets and each followee's tweets

from __future__ import division
import nltk
from nltk import FreqDist
import json
from os import listdir
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import Utilities
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy
import pandas as pd
from numpy  import array

#for each followee
    #import json data into an arrary (append each tweet)
    #join if nessecary

#import user json data into an arrary (append each tweet)
#join if nessecary

#for each followee
    #get cosine sim scores with user data

#print both scores

#front end to github i/p?
