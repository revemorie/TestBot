#imports
import os
import sys
import json
import random
import requests
import time
from flask import Flask, request

#define our flask app
app = Flask(__name__)

#Method will automatically execute when our endpoint receives a POST call
@app.route('/', methods=['POST'])
def msg_received_from_group():

  #Format the data we receive as a JSON
  data = request.get_json()
  log('{}'.format(data))
  
  #Check the text of the message sent to the chat to see if it matches our command word
  if data['text'].lower() == "who is joe":
    send_msg("Joe mama gottem")
	

  elif data['text'].lower() == "!testpic":
    send_msg_pic("Hello World!","https://www.ebony.com/wp-content/uploads/2016/07/barobama_caro_original_45230.jpg")
	
	

  return "ok", 200

 
#Sends a message to the chat that the bot originates from
def send_msg(msg):

  url  = 'https://api.groupme.com/v3/bots/post'
  
  data ={
  'bot_id' : os.getenv('GROUPME_BOT_ID'),
  'text'   : msg
  }
        
  request = requests.post(url=url, data=data)

#sends a picture and a message to the chat
#Picture URL must be registered with GroupMe first
def send_msg_pic(msg, picURL):

  url  = 'https://api.groupme.com/v3/bots/post'

  data ={
  'bot_id' : os.getenv('GROUPME_BOT_ID'),
  'text'   : msg,
  "attachments" : [
    {
      "type"  : "image",
      "url"   : picURL
    }
  ],
  'picture_url': picURL
  }

  request = requests.post(url=url, data=data)


#logging function to help debug
def log(msg):
  print(str(msg))
  sys.stdout.flush()
