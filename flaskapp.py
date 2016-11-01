#!/usr/bin/python
import os,sys
from flask import Flask, jsonify, render_template, request, abort

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/')
def webprint():
    return render_template('index.html')


@app.route('/api/sort',methods=['GET','POST'])
def get_sort():
        a = request.args.get('array')
        a = a.split(',')
        a = list(map(int, a))
        for i in range(1,len(a)):
                tmp = a[i]
                j = i
                while j>0 and a[j-1]>tmp:
                         a[j]=a[j-1]
                         j = j-1
                a[j]=tmp

        return jsonify({'result': a})

@app.route('/api/wordfreq', methods = ['GET', 'POST'])
def upload_file():
    count = 0
    a = request.form['word']
    f = request.files['file']
    for i in f.read(102400).split():
        if a == i:
                count=count+1
    return jsonify({"result":count})

@app.route('/api/prime',methods=['GET','POST'])
def get_prime():
        a = request.args.get('number')
	cou = 0
	n = int(a)
	for i in range(2,n):
        	if n%i == 0 :
        		cou = cou + 1
	if cou == 0:
        	return jsonify({'result': "Prime Number"})
	else:
		return jsonify({'result': "Not a Prime Number"})

if __name__ == '__main__':
    app.run( )

