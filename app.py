from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

'''
@app.route('/calculated', methods=["GET"])
def calculate():
    return render_template("calculated.html", grades=request.args.get("grades"))
'''


if __name__ == '__main__':
    app.run()
