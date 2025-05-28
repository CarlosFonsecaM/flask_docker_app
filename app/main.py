from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Servidor Web en Operación\nVersion Flask 2.3.2"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
