from flask import Flask
app = Flask(__name__)

@app.route("/")
def greeting():
    return "Rumiantsau python-app. Hello World 1"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8181)
