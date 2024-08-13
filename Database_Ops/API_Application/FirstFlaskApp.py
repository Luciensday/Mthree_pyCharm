from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return "Welcome to falsk application"
@app.route("/about")
def about():
    return "c394 application building session"

@app.route("/details")
def details():
    return "Python programming"

app.run(debug=True)
