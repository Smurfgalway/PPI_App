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

@app.route("/mental")
def mental():
    return render_template('Mental.html')

@app.route("/sh")
def sh():
    return render_template('sexual.html')

if __name__ == "__main__":
    app.run()