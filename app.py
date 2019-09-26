import os
import sys
import json
import random
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)
msg_choices=["Meow","Purr","Growl"]
special_array=["https://i.groupme.com/1920x1080.jpeg.bad8a2da943847b08ea013b674e520d4"]
array=["https://i.groupme.com/3024x4032.jpeg.fa24f79a44d74a6796b20a90432edba8","https://i.groupme.com/1688x2250.jpeg.cb2bf654cd614b19853bc01edb4e96b1","https://i.groupme.com/3024x4032.jpeg.d955cd324c2a473aa521d76be462e908","https://i.groupme.com/1124x1500.jpeg.338c4165e1da4698b5afddd28f8a90fb","https://i.groupme.com/563x1218.jpeg.7b7484ff24d64312ad8325f94650e544","https://i.groupme.com/1686x2250.jpeg.fcb140e1486d4bb88296cc0fe6ffc7e3"]
lastUser='123456'
@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))
  # We don't want to reply to ourselves!
  if lastUser==data['user_id']:
    msg= "Cheeto says stop spamming"
    send_msg(msg)
    
  elif data['text'].lower() == "!cheeto":
    lastUser=data['user_id']
    msg = random.choice(msg_choices)
    send_message_picture(msg,array)
    
  elif data['text'].lower() == "!notcheeto":
    lastUser=data['user_id']
    msg = random.choice(msg_choices)
    send_message_picture(msg,special_array)
    
  return "ok", 200

def send_message_picture(msg, arr):
  url  = 'https://api.groupme.com/v3/bots/post'

  rand=random.choice(arr)
  data ={
  'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
  "attachments" : [
    {
      "type"  : "image",
      "url"   : rand
    }
  ],
  'picture_url': rand
}
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()

def send_msg(msg):
  url  = 'https://api.groupme.com/v3/bots/post'
  data ={
  'bot_id' : os.getenv('GROUPME_BOT_ID'),
  'text'   : msg
        }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()

  
def log(msg):
  print(str(msg))
  sys.stdout.flush()
