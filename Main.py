import flask as fl
import sqlite3
from flask import render_template, g, request# imports the render template property which allows html pages be loaded as the template for the pages on the server

DATABASE = 'data/thisdata.db'
con = sqlite3.connect(DATABASE)
c= con.cursor()
app = fl.Flask(__name__)

#opens the database
def pullData():
    db = getattr(fl.g, '_database', None)
    if db is None:
        db = fl.g._database = sqlite3.connect(DATABASE)
    return db

#closes the database
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(fl.g, '_database', None)
    if db is not None:
        db.close()

#inserts data into the database
#-------------------------------
@app.route("/data", methods=["POST"])
def database():
    c.execute('INSERT INTO UserReviews(User, Review) VALUES(?,?)',(fl.request.form['User'],fl.request.form['Review']))
    con.commit()
    return (render_template('review.html') + str(c.fetchall()) )


#shows the contents of the database
#-------------------------------
@app.route("/show", methods=[ "GET"])
def showed():
    c.execute("Select * from UserReviews")
    thisdata = [dict(User=row[0], Review=row[1]) for row in c.fetchall()]
    return (render_template('review.html', thisdata=thisdata) + str(c.fetchall()) )

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

@app.route("/re")
def re():
    return render_template('review.html')

if __name__ == "__main__":
    app.run() # runs the app