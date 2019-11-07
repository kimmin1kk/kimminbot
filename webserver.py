from flask import Flask
from threading import Thread

client = Flask('')

@client.route('/')
def home():
    return "Webserver OK, Discord Bot Ok"

def run():
  client.run(host="0.0.0.0",port=8000)

def keep_alive():
  t=Thread(target=run)
  t.start()
