from doctest import debug

from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/students")
def student():

    data = {
        "name":"Joyal",
        "course":"bca",
        "marks":85
    }

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)