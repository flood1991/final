from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/route1")
def page1():
    return render_template('page1.html')

@app.route("/route2")
def page2():
    return render_template('page2.html')

@app.route("/route3")
def page3():
    return render_template('page3.html')

app.run()