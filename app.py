import os
from github_webhook import Webhook
from flask import Flask
from flask import request, Response
from flask import json
from github import Github
from pathlib import Path
from dotenv import load_dotenv
from slack import WebClient

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client = WebClient(token=os.environ['TOKEN'])


def send_to_slack( text_to_send ,channel="#private"):
    client.chat_postMessage(channel= channel, text=text_to_send)

app = Flask(__name__)  # Standard Flask app
webhook = Webhook(app) # Defines '/postreceive' endpoint 

@app.route("/", methods=['GET', 'POST'])        # Standard Flask endpoint 
def hello_world():
    return "Hello, World!"

#zxcvbnm

@app.route("/webhook", methods=['GET', 'POST'])
def respond():
    if request.method == 'GET':
        print("This is a GET request")
    if request.method == 'POST':
        print("this is post request")

    data = request.json
  
    if 'action' not in data:
        print(" *********** no action here *********** ")
        print(" *********** no action here *********** ")
    else:
        event_action = data['action']
        print("action is: "+ event_action)


    repo_name = data['repository']['name']
    headers_event = request.headers['X-GitHub-Event']
    event_sender = data['sender']['login']

    for commit in data['commits']:
        event_commit_comment = commit['message']
        event_timestamp = commit['timestamp']
        modified_file_name = commit['modified']
    file_name = str(modified_file_name)
    
    if headers_event == 'pull_request':
        result_str = "Event occurred is: "+ headers_event + "  Action is: " + event_action  +"  Updated repo is: "+ repo_name + "  User is: "+ event_sender +  "  Commit is: "+ event_commit_comment + "  Modified file is: " + file_name + "  Updated date and time is: " + str(event_timestamp)
    else:
        result_str = "Event occurred is: "+ headers_event + "  Updated repo is: "+ repo_name + "  User is: "+ event_sender +  "  Commit is: "+ event_commit_comment + "  Modified file is: " + file_name + "  Updated date and time is: " + str(event_timestamp)
   
    send_to_slack(result_str)
    return data    

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)