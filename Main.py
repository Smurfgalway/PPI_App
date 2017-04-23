import flask as fl
from flask import render_template

app = fl.Flask(__name__)

#Loads the Index html page as my render template loading on my server 
@app.route("/")
def name():
    return render_template('Index.html')
#set up for my button navigation for my map loading
@app.route("/map")
def map():
    return render_template('Main.html')

@app.route("/map1")
def map1():
    return render_template('Map1.html')

@app.route("/map2")
def map2():
    return render_template('Map2.html')

@app.route("/map3")
def map3():
    return render_template('Map3.html')

@app.route("/mental")
def mental():
    return render_template('Mental.html')

@app.route("/sh")
def sh():
    return render_template('sexual.html')

if __name__ == "__main__":
    app.run()