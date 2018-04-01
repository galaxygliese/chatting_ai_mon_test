#-*- coding:utf-8 -*-

from gensim.models import word2vec
from gensim.models import KeyedVectors
from nltk.tokenize import sent_tokenize
from pprint import pprint
import numpy as np

class w2v:
    def __init__(self, demission, filename=None, train=False):
       self.name = "model_word.h5"
       if train:
         sent=word2vec.LineSentence(filename)
         model = word2vec.Word2Vec(sent , size=demission, min_count=1, window=5)
         model.save(self.name)
         self.model=model
       else:
         model = word2vec.Word2Vec.load(self.name)
         self.model = model
    def word_vec(self, words):
       return [self.model.wv[word] for word in words ]    
    
    def word_net(self, words):
        return { key: self.model.most_similar(positive=[key]) for key in words }        

    def word_neigh(self, wordlist):
        try:
           return self.model.most_similar(positive=wordlist)   
        except KeyError:
           N = np.random.randint(0,2)
           if N <1:
              return "сайн мэдэхгүй байна." 
           else:
              return "..."

    def word_analyse(self, pos, neg):
        return self.model.most_similar(positive=pos, negative=neg)

    def vocab(self):
        return self.model.wv.vocab

if __name__ == '__main__':
   w2v = w2v(10, filename='train text' , train=True)
   o = w2v.word_neigh(['тэнгэр'])
   print(o)

