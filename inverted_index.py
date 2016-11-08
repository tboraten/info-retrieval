#!/usr/bin/python
#############################################################
##
##  Travis Boraten
##  10/4/2013
##
##  Homework 1: Part 3:  The Goal of this script is to consolidate work from previous parts
##  and build an inverted index by looping through the document, tracking the frequency, and the document ID
##  was found in, then merging
##
##  Entire corpus must be in the subdirectory named cacm with the script to work.
##
##


import os
import nltk
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from urllib import urlopen



tokens = []
merged = []
os.chdir("cacm")
print 'Corpus importing...'
file_count = 1

#loop runs through each html file and adds all the tokens to a single list
for files in os.listdir("."):
    if files.endswith(".html"):
        html = open(files).read()
        text = nltk.clean_html(html)
        sent_tokens = [word_tokenize(s) for s in sent_tokenize(text)]
        tokens = [token for sentence in sent_tokens for token in sentence] + tokens
        words = [w.lower() for w in tokens if w.isalpha()]        #Attempt to grab only 'words'

        porter = nltk.PorterStemmer()
        stopwords = set(nltk.corpus.stopwords.words('english'))   #Retrieve stop words
        filtered_words = [w for w in words if not w in stopwords] #Remove them
        stemmed_words = [porter.stem(w) for w in filtered_words]  #Stem words

        #stemmed_words at this point needs to remove
        #store <term,docid>
        doc_listing = {}
        for w in stemmed_words:
          if w not in doc_listing:
            doc_listing[w] = file_count

        ##complete step two of inverted index(merge + sort)
        merged = [(w,f) for (w,f) in doc_listing.items()] + merged
        merged.sort()

        #TEST SENTINEL FOR DEBUGGINGS
        #SO WE DON'T RUN ON THE ENTIRE CORPUS EVERYTIME
        if file_count == 4:
#            first = doc_listing;
            break;

        #Make sure Doc ID is updated
        file_count += 1 
        #print files
print 'Complete.'

#After this loop we have the
#term document frequency (how many documents the term is in)
term_docfreq = {}
for w in merged:
  if w[0] not in term_docfreq:
    term_docfreq[w[0]] = 0
  term_docfreq[w[0]] +=1

#Create the final postings list
posting_list = {}
for w in merged:
  if w[0] not in posting_list:
    posting_list[w[0]] = []
  posting_list[w[0]].append( w[1])


term_docfreq = [(w,f) for (w,f) in term_docfreq.items()]
term_docfreq.sort()
posting_list = [(w,f) for (w,f) in posting_list.items()]
posting_list.sort()

##Writing output format not debugged yet
### Open a file
##fo = open("/map1.txt", "wb")
##fo.write( "Soo...python is awesome..btw\n");
##for w in term_docfreq:
##    fo.write('\n'.join('%s %s' % x for x in term_docfreq[w]))
##    fo.write( " -> ")
##    fo.write('\n'.join('%s %s' % x for x in posting_list[w]))
### Close opend file
##fo.close()
