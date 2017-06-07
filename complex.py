from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    cities = ["Nairobi","Mombasa","joBurg","Abuja","Lagos","London","Baghdad"]
    return render_template("index.html",cities= cities)


if __name__ == '__main__':
    app.run(port=1002)
