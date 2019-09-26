import os
import sys
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)
global array=["https://i.groupme.com/3024x4032.jpeg.d955cd324c2a473aa521d76be462e908","https://i.groupme.com/1124x1500.jpeg.338c4165e1da4698b5afddd28f8a90fb","https://i.groupme.com/563x1218.jpeg.7b7484ff24d64312ad8325f94650e544","https://i.groupme.com/1686x2250.jpeg.fcb140e1486d4bb88296cc0fe6ffc7e3"]
@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))

  # We don't want to reply to ourselves!
  if data['text'].lower() == "!cheeto":
    msg = 'Meow'
    send_message(msg)

  return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  rand=random.choice(array)
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
  
def log(msg):
  print(str(msg))
  sys.stdout.flush()
