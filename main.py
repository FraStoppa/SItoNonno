from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_page():
    return "<h1>Hello world!!</h1>"


@app.route("/about")
def about_us():
    return "<p>Questi siamo noi</p>"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
