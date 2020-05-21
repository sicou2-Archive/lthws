from flask import Flask
app = Flask(__name__)


@app.route('/')
def howdy_dammit():
    greeting = "dammit!"
    return f"Howdy {greeting}!"


if __name__ == "__main__":
    app.run()
