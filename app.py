from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", names=["Bob", "Charlie", "David"])


app.run(host="localhost", debug=True)
