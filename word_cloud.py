#!/usr/bin/python
#############################################################
##
##  Travis Boraten
##  10/4/2013
##
##  Homework 1: Part 2: Word Clouds
##
##  Script implements a function to turn words into singular format.
##  The remaining two functions allow you to make words singular, or stemmed, given another list of words to affect
##
##




import nltk
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from urllib import urlopen
from nltk.stem import WordNetLemmatizer

porter = nltk.PorterStemmer()
lemmer = WordNetLemmatizer()

#############################################################
##Function uses the porter stemmer step1ab function to make words singular
###############################################################
def plur(self,porter):
    porter.b = self
    porter.k = len(self)-1
    porter.k0 = 0
    porter.step1ab()
    return porter.b[porter.k0:porter.k+1]

#############################################################
##Function uses plur to turn words into their singular form
###############################################################
def singularize(words,type_list):
    singular = []
    for n in words:
        if n in noun_list:
            singular.append(plur(n,porter))
        else:
            singular.append(n)

    return singular

#############################################################
##Function lementizes words found in type_list
###############################################################
def singularize_lem(words,type_list):
    singular = []
    for n in words:
        if n in noun_list:
            singular.append(lemmer.lemmatize(n))
        else:
            singular.append(n)

    return singular

#############################################################
##Code Stripped from nltk book Chapter03
###############################################################
def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                  if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].keys()[:]) for tag in cfd.conditions())
###############################################################


#url = "http://oucsace.cs.ohiou.edu/~razvan/courses/ir6900/cs-wordle-input.txt"
#html = urlopen(url).read()
#text = nltk.clean_html(html)
with open("C:\Users\Travasi\Dropbox\Python\export_mail.txt") as f:
    text = f.readlines()
f.close()

text2 = ""
for n in text:
    if "Body:" in n:
        text2 = text2 + n[5:]

f = open('export_words2.txt', 'w')
f.write(text2)
f.close()
exit()

#text = nltk.clean_html(text2)
sent_tokens = [word_tokenize(s) for s in sent_tokenize(text2)]
tokens = [token for sentence in sent_tokens for token in sentence]
words = [w.lower() for w in tokens if w.isalpha()]
speech = nltk.pos_tag(words)

find_nouns = findtags('NN', speech)
reduce_nouns = [find_nouns[w] for w in find_nouns]

noun_list = []
for n in reduce_nouns:
	for w in n:
		noun_list.append(w)

singular_speech = singularize(words, noun_list)
singular_speech = singularize(words, words)

#print singular_speech
