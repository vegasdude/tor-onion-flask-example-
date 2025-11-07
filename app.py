from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from a Tor hidden service!"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
