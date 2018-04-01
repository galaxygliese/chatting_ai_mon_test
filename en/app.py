#-*- coding:utf-8 -*- 

from flask import Flask, render_template, request, url_for
import numpy as np
import d2v as d
import json

app = Flask(__name__)
massages = []
input_text=""

d2v = d.d2v(10)

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/chat?mess=<text>')
@app.route('/chat', methods=['GET', 'POST'])
def index_text():
    if request.method == 'POST':
       res = request.form["mess"]
       input_text = res
       output_text = output_api( d2v.model.most_similar(d2v.doc_vec(input_text) )  )
       try:
           o = output_text.decode('utf-8')
       except UnicodeEncodeError:
           o = "UnKnownChar"
       massages.append({'user':res, 'AI': o })
    return render_template('index_text.html', massages=massages)

def output_api(out):
    N = np.random.randint(0,3)
    return out[N][0]


if __name__ == '__main__':
   app.run()

