import os
import sys
import json
import random
import requests
from urllib.parse import urlencode, unquote
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)
msg_choices=["Meow","Purr","Growl","lööps bröther"]
leaderboardNumber=[]
leaderboardName=[]
leaderboardId=[]
special_array=["https://i.groupme.com/1500x2250.jpeg.fbc08bc4eff14029a23c7e684d602f1a","https://i.groupme.com/457x399.jpeg.5089079d5a4c4b5abae69ba1d77d413c","https://i.groupme.com/1266x2250.jpeg.76f6311bf2ef4d3e9fd75bf2d6fc8f0c","https://i.groupme.com/1280x720.jpeg.38d93ff6f1304ba2b94c0aaf602f990b","https://i.groupme.com/1125x1500.jpeg.09c008a31f954c1db86159d9c62c0a39","https://i.groupme.com/873x654.jpeg.95c9ee5907aa4822b8200b4349dbe332","https://i.groupme.com/1920x1080.jpeg.bad8a2da943847b08ea013b674e520d4","https://i.groupme.com/1224x1632.jpeg.67b08560e7ff4f07ae62932124137560"]
array=["https://i.groupme.com/1122x2208.jpeg.c432a6c9addc4d2fb5492c5782457611","https://i.groupme.com/1536x2048.jpeg.82d1b1bf281b43779ca5027cfa3c2288","https://i.groupme.com/4032x3024.jpeg.565584ed54cc46419d69f3f40315f5ee","https://i.groupme.com/1688x2250.jpeg.783a2dd5d50d47cc928d078f4c2541bb","https://i.groupme.com/3024x4032.jpeg.9e164408e4894f5b9405c3ababafb111","https://i.groupme.com/1688x2250.jpeg.de0ef3f47aa94149a7ce8ebf1e0cce39","https://i.groupme.com/4032x3024.jpeg.684ffe5536a44b69bfc88c4567e10515","https://i.groupme.com/1124x1500.jpeg.94eeffa8faec4036bd670e1a8837e42f","https://i.groupme.com/1798x1126.jpeg.5c5f21ace93e4e76add41a30f6457680","https://i.groupme.com/3024x4032.jpeg.fa24f79a44d74a6796b20a90432edba8","https://i.groupme.com/1688x2250.jpeg.cb2bf654cd614b19853bc01edb4e96b1","https://i.groupme.com/3024x4032.jpeg.d955cd324c2a473aa521d76be462e908","https://i.groupme.com/1124x1500.jpeg.338c4165e1da4698b5afddd28f8a90fb","https://i.groupme.com/563x1218.jpeg.7b7484ff24d64312ad8325f94650e544","https://i.groupme.com/1686x2250.jpeg.fcb140e1486d4bb88296cc0fe6ffc7e3"]
bbbArray=["https://v.groupme.com/20753497/2019-09-30T18:17:02Z/39b4c006.348x240r.mp4"]
bwarr=["https://i.groupme.com/1078x584.jpeg.825dce815bbe489a9dacccdca1e807b6"]
gwarr=["Honestly, I’ve always loved cheesesteaks. They’re kind of my go-to when there’s nothing else to have at restaurants, but obviously it’s a little different when you’re out in Philly and have an authentic Philly cheesesteak.","I remember just praying, ‘Dear Lord, please let me grow to be at least 6 feet.’","I’m a competitive son of a gun. I don’t like losing. I want to be the best out there.","I view every day just as an opportunity.","I don't get nervous.","All I care about is winning."]
@app.route('/', methods=['POST'])
def webhook():
  
  data = request.get_json()
  log('Recieved {}'.format(data))
  # We don't want to reply to ourselves!
    
  if data['text'].lower() == "!cheeto":
    msg = random.choice(msg_choices)
    send_message_picture(msg,array)
    
  elif data['text'].lower() == "!notcheeto":
    msg = random.choice(msg_choices)
    send_message_picture(msg,special_array)


  elif data['text'].lower() == '!live':
    r=requests.get("http://16fb9c95.ngrok.io")
    log('returned')
    
  elif data['text'].lower() == '!bigbootybitches':
    msg ="https://v.groupme.com/20753497/2019-09-30T18:17:02Z/39b4c006.348x240r.mp4"

    send_msg(msg)
    

  elif data['text'].lower() == '!help':
    
    msg ="!help- Shows this text\n!cheeto- Displays a random photo of cheeto\n!notcheeto- Displays a random photo of something that is not cheeto\n!live- Generates a live gif of whatever the PiCamera is pointing towards (hopefully cheeto)\n!bigbootybitches- I GOT BIG BOOTY BITCHES\n!leaderboard- THIS IS IN BETA"

    send_msg(msg)

  elif data['text'].lower() == "!leaderboard":
    r=requests.get("https://api.groupme.com/v3/groups/21164167",headers={'Content-Type': 'application/json','X-Access-Token': os.getenv('AS_TOKEN')})
    
    members=(json.loads(r.text))['response']['members']
    for i in members:
      leaderboardId.append(i['user_id'])
      leaderboardName.append(i['nickname'])
      
    l=requests.get("https://api.groupme.com/v3/groups/21164167/likes?period=week",headers={'Content-Type': 'application/json','X-Access-Token': os.getenv('AS_TOKEN')})
    print((json.loads(l.text)))
    messages=(json.loads(l.text))['response']['messages']
    for j in messages:
      likes=j['favorited_by']
      user=j['user_id']
      for k in likes:
        leaderboardNumber[leaderboardId.index(user)]+=1

    msg=""
    for i in range(len(leaderboardId)):
      msg+=str(leaderboardName[i])+" Recieved "+str(leaderboardNumber[i])+" Likes this week\n"

    send_msg(msg)
    leaderboardNumber.clear()
    leaderboardName.clear()
    leaderboardId.clear()
    
    
  '''
  elif ("i’m" in data['text'].lower() or "i'm" in data['text'].lower() )and data['sender_type']!='bot':

    amNum=data['text'].lower().find("i'm")
    if amNum==-1:
      amNum=data['text'].lower().find("i’m")
      
    am=data['text'][amNum+4:]
    msg="Hi "+am+", I'm CheetoBot"
    send_msg(msg)
   '''
  return "ok", 200


@app.route('/picture', methods=['POST'])
def picWebhook():
  data = request.get_data()
  log('Recieved {}'.format(data))
  msg=""
  url=unquote(str(data,'utf-8')[8:])
  gened_pic=[url]
  send_message_picture(msg,gened_pic)

  return "ok", 200

@app.route('/qb', methods=['POST'])
def qbWebhook():
  data = request.get_json()
  log('Recieved {}'.format(data))
 
  if data['text'].lower() == '!goodwentz':
    msg = '"'+random.choice(gwarr)+'"-Carson Wentz'
    send_msg_wentz(msg)
    
  if data['text'].lower() == '!badwentz':
    msg =""
    send_message_picture_wentz(msg,bwarr)
  
  return "ok", 200


def send_message_picture_wentz(msg, arr):
  url  = 'https://api.groupme.com/v3/bots/post'

  rand=random.choice(arr)
  data ={
  'bot_id' : os.getenv('WENTZ_ID'),
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
  
def send_msg_wentz(msg):
  url  = 'https://api.groupme.com/v3/bots/post'
  data ={
  'bot_id' : os.getenv('WENTZ_ID'),
  'text'   : msg
        }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()



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


def gen_picture(data):
  url  = 'https://image.groupme.com/pictures'
  headers = {
    'X-Access-Token': os.getenv('AS_TOKEN'),
    'Content-Type': 'image/jpeg',
  }
  
  request = Request(url, data=data,headers=headers)
  js = urlopen(request).read().decode()
  toReturn=json.loads(js)
  log(toReturn['payload']['url'])
  return toReturn['payload']['url']
  
def log(msg):
  print(str(msg))
  sys.stdout.flush()
