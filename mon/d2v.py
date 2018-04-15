#-*- coding:utf-8 -*-

from gensim.models.doc2vec import Doc2Vec 
from gensim.models.doc2vec import TaggedDocument
from nltk.tokenize import sent_tokenize
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

class d2v:
    def __init__(self, demission, filename=None, train=False):
       self.name = 'model_new.h5'
       if train:
         with open(filename, 'r') as f:
              trainings = [TaggedDocument(words = sent_tokenize(data.decode('utf-8')) ,tags = [i]) for i,data in enumerate(f)]
         model = Doc2Vec(trainings , size=demission, min_count=1, window=5)
         model.save(self.name)
         self.model=model
       else:
         model = Doc2Vec.load(self.name)
         self.model = model
    def doc_vec(self, docs):
       return [self.model.infer_vector(doc) for doc in docs ]    
    
    def doc_neigh(self, doclist):
        try:
          return self.model.most_similar(doclist)    
        except KeyError:
          if np.random.randing(0,2) > 1:
             return "I couldn't understand"
          else:
             return "..."


if __name__ == '__main__':
   #with open('example.txt') as f:
   #     text = f.read()
   d2v = d2v(2, filename='training.txt')
   #pprint(d2v.model.most_similar(d2v.doc_vec('what is the AI?') ) )
   pprint(d2v.model.most_similar(d2v.doc_vec('what are you doing') ) )


