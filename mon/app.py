#-*- coding:utf-8 -*- 

from flask import Flask, render_template, request, url_for
import w2v2 as w
import json

app = Flask(__name__)
massages = []
input_text=""

w2v = w.w2v(10)

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/chat?mess=<text>')
@app.route('/chat', methods=['GET', 'POST'])
def index_text():
    if request.method == 'POST':
       res = request.form["mess"]
       input_text = res
       output_text = w2v.word_neigh([input_text])
       massages.append({'user':res, 'AI':output_text.decode('utf-8') })
    return render_template('index_text.html', massages=massages)


if __name__ == '__main__':
   app.run()

