import flask as fl
from flask import render_template

app = fl.Flask(__name__)

@app.route("/")
def name():
    return render_template('Index.html')


if __name__ == "__main__":
    app.run()