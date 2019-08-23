from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
    return("Hello World")

@app.route('/verification', methods = ["POST"])
def getting_challenge():
    slack_req = request.get_json()['challenge']
    response = {'challenge':slack_req}
    return(response)


if __name__ == "__main__":
    app.run()