from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome Ninja Boss!</h1>
    <p>My first Python website!</p>
    """

app.run(debug=True)