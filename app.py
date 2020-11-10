import os
from github_webhook import Webhook
from flask import Flask
from flask import request, Response
from flask import json
from github import Github
from pathlib import Path
from dotenv import load_dotenv
from slack import WebClient

#env_path = Path('.') / '.env'
#load_dotenv(dotenv_path=env_path)
#client = WebClient(token=os.environ['TOKEN'])


#def send_to_slack( text_to_send ,channel="#private"):
 #   client.chat_postMessage(channel= channel, text=text_to_send)

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app) # Defines '/postreceive' endpoint

@app.route("/", methods=['GET', 'POST'])        # Standard Flask endpoint
def hello_world():
    return "Hello, World!"


@app.route("/webhook", methods=['GET', 'POST'])
def respond():
    print("** New Payload from Github **")
    #print(request.json)
    #return Response(status=200)

    data = request.json
    print(data)
    return data

#@webhook.hook()        # Defines a handler for the 'push' event
#def on_push(data):
 #   print("Got push with: {0}".format(data))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)