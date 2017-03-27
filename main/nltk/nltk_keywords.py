from __future__ import division
import nltk
from nltk.corpus import brown
from flask import jsonify
from nltk import word_tokenize

def test():
    return count_file()

def lexical_diversity(text):
    return len(text) / len(set(text))

def count_words():
    news_text = brown.words(categories='news')
    # news_text = ['can', 'Fulton', 'County', 'Grand', 'Jury', 'said']
    fdist = nltk.FreqDist([w.lower() for w in news_text])
    modals = ['can', 'could', 'may', 'might', 'must', 'will']
    print(news_text)
    for m in modals:
        print(m + ':', fdist[m])
    return build_json(fdist,modals)

def count_file():
    f = open('text/myjd2.txt')
    raw = f.read()
    tokens = word_tokenize(raw)
    fdist = nltk.FreqDist([w.lower() for w in tokens])
    modals = set(tokens)
    print(fdist)
    for m in modals:
        print('tokens count m: ' + str(tokens.count(m)))
        print('len tokens: ' + str(len(tokens)))
        print(m + ':', tokens.count(m) / len(tokens))
    return build_json(fdist, modals)

def build_json(fdist, modals):
    ls = []
    rs = dict()
    rs['code'] = '200'
    rs['result'] = ls
    for m in modals:
        result = dict()
        result['word'] = m
        result['weight'] = fdist[m]
        ls.append(result)
    return jsonify(rs)





