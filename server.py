from urllib import request
from flask import Flask, render_template, session, redirect 
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.post('/process')
def insert_info():
    session['name']=request.form['name']
    session['dojo_location']=request.form['dojo_location']
    session['fav_language']=request.form['fav_language']
    session['comment']=request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__=='__main__':
    app.run(debug=True, host='localhost', port=5000)