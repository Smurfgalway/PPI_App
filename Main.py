import flask as fl
from flask import render_template # imports the render template property which allows html pages be loaded as the template for the pages on the server

app = fl.Flask(__name__)

#Loads the Index html page as my render template loading on my server 
@app.route("/")
def name():
    return render_template('Index.html')
#set up navigation for my main map page
@app.route("/map")
def map():
    return render_template('Main.html')
#for navigation to map 1
@app.route("/map1")
def map1():
    return render_template('Map1.html')
#for navigation to map 2
@app.route("/map2")
def map2():
    return render_template('Map2.html')
#for navigation to map 3
@app.route("/map3")
def map3():
    return render_template('Map3.html')
#for navigation to map 4
@app.route("/map4")
def map4():
    return render_template('Map4.html')
# navigation for the mental health hub
@app.route("/mental")
def mental():
    return render_template('Mental.html')
# navigation for the sexual health hub
@app.route("/sh")
def sh():
    return render_template('sexual.html')

if __name__ == "__main__":
    app.run() # runs the app