from flask import Flask, render_template, request, session, redirect 
app= Flask(__name__)
app.secret_key = '3564fgfgsdg875689696845674633'


@app.route('/')
def index():
    return render_template('index.html')

@app.post('/process')
def insert_info():
    session['name']=request.form['name']
    session['dojo_location']=request.form['dojo_location']
    session['fav_language']=request.form['fav_language']
    session['comment']=request.form['comment']
    # redirect takes a route
    return redirect('/process')

@app.get('/process')
def result():
    return render_template('result.html')

if __name__=='__main__':
    app.run(debug=True, host='localhost', port=5000)