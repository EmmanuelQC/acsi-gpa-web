from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    # return render_template("index.html")
    return "Hello, World"

'''
@app.route('/calculated', methods=["GET"])
def calculate():
    return render_template("calculated.html", grades=request.args.get("grades"))
'''


if __name__ == '__main__':
    app.run()
