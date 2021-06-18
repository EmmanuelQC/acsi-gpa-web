from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return render_template("index.html")
    return <h1>ACS GPA</h1><body><h2>Enter Your Grades Here:</h2><select><option>7</option><option>6</option><option>5</option></select><h3>Your average: 6.9</h3>

'''
@app.route('/calculated', methods=["GET"])
def calculate():
    return render_template("calculated.html", grades=request.args.get("grades"))
'''


if __name__ == '__main__':
    app.run()
