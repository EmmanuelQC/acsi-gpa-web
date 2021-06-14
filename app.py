from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/calculated', methods=["GET"])
def calculate():
    return render_template("calculated.html", grades=request.args.get("grades"))


if __name__ == '__main__':
    app.run()
