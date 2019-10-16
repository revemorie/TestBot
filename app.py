import os
import sys
import json
import random
import requests
import time
from urllib.parse import urlencode, unquote
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))
  # We don't want to reply to ourselves!
  
  if data['text'].lower() == "!test":
   send_msg("hey")

  return "ok", 200

  
def send_msg(msg):
  url  = 'https://api.groupme.com/v3/bots/post'
  data ={
  'bot_id' : ,
  'text'   : msg
        }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()


def log(msg):
  print(str(msg))
  sys.stdout.flush()
