import os 
import time
import slack

slack_token = os.environ.get("SLACK_BOT_TOKEN")
client = slack.WebClient(token = slack_token)

channels = client.conversations_list()
if channels.get('ok') == True:
    for c in channels['channels']:
        print(c['name'], c['id'])
client.chat_postMessage(
    channel="CMNC4AMRB",
    text = "Testing 123"
)
