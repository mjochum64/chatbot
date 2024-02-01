import sys
import socket
from tweepy import StreamListener, OAuthHandler
from tweepy import API
from tweepy import Stream

# Twitch Chat IRC Server
irc_server = "irc.chat.twitch.tv"
irc_port = 6667
irc_timeout = 10

# Authenticate to Twitch
consumer_key = 'your-consumer-key'
consumer_secret = 'your-consumer-secret'
access_token = 'your-access-token'
access_token_secret = 'your-access-token-secret'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

# Connect to Twitch Chat IRC Server
s = socket.socket()
s.connect((irc_server, irc_port))
s.settimeout(irc_timeout)

nickname = "your-bot-username"
channel = "#your-channel"

# Send Nick to Twitch Chat IRC Server
s.send("NICK {0}\\r\\n".format(nickname).encode('utf-8'))
s.send("JOIN {0}\\r\\n".format(channel).encode('utf-8'))

def on\\_message(msg):
command = msg['command']
params = msg['params']
tags = msg['tags']

if command == 'PRIVMSG':
if nickname.lower() in params[0].lower():
user = params[0][1:] # Remove the leading colon
message = params[1]
print(f'{user}: {message}')
# Add your bot commands here
if message.startswith('!hello'):
s.send("PRIVMSG #{0} :Hello, {1}!\\r\\n".format(channel, user).encode('utf-8'))

class MyStreamListener(StreamListener):
def on\\_message(self, status):
on\\_message(status)

myStreamListener = MyStreamListener()
myStream = Stream(auth, myStreamListener)
myStream.filter(track=[channel])

