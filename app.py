from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def getting_challenge():
    slack_req = json.loads(request.form.get('payload'))
    response = {"challenge": slack_req['challenge']}
    return(response)

if __name__ == "__main__":
    app.run()