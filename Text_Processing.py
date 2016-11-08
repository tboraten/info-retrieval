#!/usr/bin/python
#############################################################
##
##  Travis Boraten
##  10/4/2013
##
##  Homework 1: Part 1:  Script Should print out all the requested information
##  minus the figures requested.
## 
##  Entire corpus must be in the subdirectory named cacm with the script to work.
##
##


import os
import nltk
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from urllib import urlopen



tokens = []
os.chdir("cacm")
print 'Corpus importing...'
half = 1 #counter to see when we are at half way through the corpus

#loop runs through each html file and adds all the tokens to a single list
for files in os.listdir("."):
    if files.endswith(".html"):
        html = open(files).read()
        text = nltk.clean_html(html)
        sent_tokens = [word_tokenize(s) for s in sent_tokenize(text)]
        tokens = [token for sentence in sent_tokens for token in sentence] + tokens

        #if we are half way done, save the tokens
        if len(os.listdir(".")) / 2 == half:
            half_tokens = tokens
            #print half

        half += 1
        #print files
print 'Complete.'

words = [w.lower() for w in tokens if w.isalpha()]
word_counts = {}
for w in words:
  if w not in word_counts:
    word_counts[w] = 0
  word_counts[w] +=1

#rank the documents
ranked = [(f,w) for (w,f) in word_counts.items()]
ranked.sort()
ranked.reverse()

##Calculate the states
happax_legomena = 0
dis_legomena = 0
for w in word_counts:
    if word_counts[w] == 1:
        happax_legomena += 1
    elif word_counts[w] == 2:
        dis_legomena += 1

common_words = 0.0
for w in list(ranked[:20]):
  common_words += word_counts[w[1]]
  

#print file_name[5:]
print '------------------------------'
print '1. Text Processing: Parts 1-5'
print '------------------------------'
print 'Tokens: %d' % len(words)
print 'Vocab: %d' % (len(sorted(set(words))))
print 'Happax Legomena: %d' % (happax_legomena)
print 'Dis Legomena: %d' % (dis_legomena)
print 'Top 20 common token types:'
print ranked[:20]
print '%.2f%%' % ((common_words/len(words)*100))



########################################
## 6-9
#Filter and stem the entire corpus
porter = nltk.PorterStemmer()
stopwords = set(nltk.corpus.stopwords.words('english'))   #Retrieve stop words
filtered_words = [w for w in words if not w in stopwords] #Remove them
stemmed_words = [porter.stem(w) for w in filtered_words]  #Stem words

word_counts = {}
for w in stemmed_words:
  if w not in word_counts:
    word_counts[w] = 0
  word_counts[w] +=1

#Find all words that appeared only once, and twice
happax_legomena = 0
dis_legomena = 0
for w in word_counts:
    if word_counts[w] == 1:
        happax_legomena += 1
    elif word_counts[w] == 2:
        dis_legomena += 1

ranked = [(f,w) for (w,f) in word_counts.items()]
ranked.sort()
ranked.reverse()

#filter and stem half the corpus
half_words = [w.lower() for w in half_tokens if w.isalpha()]
half_filtered_words = [w for w in half_words if not w in stopwords]
half_stemmed_words = [porter.stem(w) for w in half_filtered_words]

half_word_counts = {}
for w in half_stemmed_words:
  if w not in half_word_counts:
    half_word_counts[w] = 0
  half_word_counts[w] +=1

#Find all words that appeared only once, and twice
half_happax_legomena = 0
half_dis_legomena = 0
for w in half_word_counts:
    if half_word_counts[w] == 1:
        half_happax_legomena += 1
    elif half_word_counts[w] == 2:
        half_dis_legomena += 1

half_ranked = [(f,w) for (w,f) in half_word_counts.items()]
half_ranked.sort()
half_ranked.reverse()

print '------------------------------'
print '1. Text Processing: Parts 6-9 - Stopwords & Stemming'
print '------------------------------'
print 'Tokens (FULL): %d' % len(words)
print 'Tokens (Half): %d' % len(half_words)
print 'Vocab (FULL): %d' % (len(sorted(set(stemmed_words))))
print 'Vocab (Half): %d' % (len(sorted(set(half_stemmed_words))))
print 'Happax Legomena (FULL): %d' % (happax_legomena)
print 'Happax Legomena (Half): %d' % (half_happax_legomena)
print 'Dis Legomena (FULL): %d' % (dis_legomena)
print 'Dis Legomena (Half): %d' % (half_dis_legomena)
print 'Top 20 common token types (FULL):'
print ranked[:20]
print 'Top 20 common token types (Half):'
print half_ranked[:20]



    
