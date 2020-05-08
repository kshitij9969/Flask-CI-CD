from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, my name is Kshitij Singh."


if __name__ == '__main__':
    app.run(debug=True)