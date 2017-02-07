# -*- coding:utf-8 -*-
import nltk

nltk.corpus.gutenberg.fileids()
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
len(emma)
emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
emma.concordance("surprize")

from nltk.corpus import gutenberg

gutenberg.fileids()
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print int(num_chars / num_words), int(num_words / num_sents), int(num_words / num_vocab), fileid

macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')

