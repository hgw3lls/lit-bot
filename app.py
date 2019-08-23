from flask import Flask, request, status
import json

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    return('Hello World')

@app.route('/', methods=["POST"])
def getting_challenge():
    slack_req = json.loads(request.form.get('payload'))
    response = slack_req['challenge']
    return(status.HTTP_200_OK, "Content-type: text/plain", response)


if __name__ == "__main__":
    app.run()


