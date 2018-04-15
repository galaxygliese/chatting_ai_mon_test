#-*- coding:utf-8 -*-

import commands
import re
from pprint import pprint

def translate(text, source, _to):
    try:
      res =  commands.getoutput("translate -d '{0}' -s '{1}' '{2}'".format(_to, source, text))
      output = res.split('[{0}]'.format(_to))[1].split('[pron.]')[0]
      return output[1:-1]
    except Exception as e:
      print e
      return "couldn't translate"

if __name__ == '__main__':
   #o = translate('сайн байна уу?', 'mn', 'en')
   print type('сайн байна уу?')
   o = translate('юу хийж байна', 'mn', 'en')
   pprint(o)

