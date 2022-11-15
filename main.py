from flask import Flask, render_template

MyNameCard = Flask(__name__)

@MyNameCard.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    MyNameCard.run(debug=True)