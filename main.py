from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_page():
    return "<h1>Hello world!!</h1>"


@app.route("/contatti")
def contact():
    return "<h2>Questa è la pagina dei contatti</h2>"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
