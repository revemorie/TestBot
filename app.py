import os
import sys
import json
import random
import requests
import time

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def msg_received_from_group():

  data = request.get_json()
  log('{}'.format(data))
  
  if data['text'].lower() == "!test":
   send_msg("Hello World!")

  return "ok", 200

  
def send_msg(msg):

  url  = 'https://api.groupme.com/v3/bots/post'
  
  data ={
  'bot_id' : os.getenv('GROUPME_BOT_ID'),
  'text'   : msg
  }
        
  request = requests.post(url=url, data=data)


def log(msg):
  print(str(msg))
  sys.stdout.flush()
