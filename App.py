import flask
from flask import render_template

# Create app
app = flask.Flask(__name__)
app.config["DEBUG"] = False

# Routes
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

app.run(host="0.0.0.0", port=80)