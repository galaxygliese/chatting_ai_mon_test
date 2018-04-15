#-*- coding:utf-8 -*- 

from flask import Flask, render_template, request, url_for
from langdetect import detect
import d2v as d
import translator as t
import numpy as np
import json
import re

app = Flask(__name__)
massages = []
input_text=""
d2v = d.d2v(10)

def is_en(text):
    return any(re.findall('\w+', text))

def is_mon(text):
    return any(re.findall('[А-я]+', text))

def text_clean(text):
    if any(re.findall('( : )', text)):
      return text.split(':')[1]
    else:
      return text

def response(text):
    text = text.encode('utf-8')
    try:
       if is_en(text):
         output = d2v.model.most_similar(d2v.doc_vec(str(text)) )[0][0]         

       elif is_mon(text):
         input_text = t.translate(text, 'mn', 'en')
         o = d2v.model.most_similar(d2v.doc_vec(str(input_text)) )[0][0]
         print o
         o = text_clean(o)
         output = t.translate(str(o), 'en', 'mn')

       else: 
         lang = detect(text)
         input_text = t.translate(text, str(lang), 'en')
         o = d2v.model.most_similar(d2v.doc_vec(str(input_text)) )[0][0]
         o = text_clean(o)
         output = t.tranlate(o, 'en', str(lang))
        
    except Exception as e:
         print e
         res = ["Sorry, I couldn't understant", "...", "уучилаарай би ойлгосонгүй"]
         output = res[np.random.randint(len(res))]

    return text_clean(output)

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/chat?mess=<text>')
@app.route('/chat', methods=['POST'])
def index_text():
    if request.method == 'POST':
       res = request.form["mess"]
       input_text = res
       output_text = response(input_text)
       massages.append({'user':res, 'AI':output_text.decode('utf-8') })
    return render_template('index_text.html', massages=massages)


if __name__ == '__main__':
   app.run()

