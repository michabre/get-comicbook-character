#
# Dependencies
#
import os
import json
import requests
import urllib.request
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, jsonify, render_template

#
# Helper functions
# helpers.py
#
from helpers import generateHash, getUnixTimestamp

#
# Environment Variables
#
load_dotenv(find_dotenv())

pub = os.environ.get("PUBLIC_KEY")
priv = os.environ.get("PRIVATE_KEY")
url = os.environ.get("MARVEL_URL")

# Flask
app = Flask(__name__)

#
# Default page
#
@app.route('/')
def index():
  return render_template('index.html', title='Get A Comicbook Character')

#
# Request JSON object on a Character
#
@app.route('/character/<character>', methods=['GET', 'POST'])
def getCharacters(character):
  ts = getUnixTimestamp()
  payload = {
    'ts': ts, 
    'apikey': pub,
    'hash': generateHash(ts, priv, pub),
    'name': character,
    'orderBy': 'name'
  }
  r = requests.get(url+"/characters", params=payload)
  response = r.json()

  if(response["data"]["count"] > 0):
    return response
  
  return {"message": "No results."}

#
# Compare 2 characters and check what comics they have both appeared in.
# Need to use character IDs to make this request, not character names.
#
@app.route('/compare/<character1>/<character2>')
def compareCharacters(character1, character2):
  ts = getUnixTimestamp()

  payload = {
    'sharedAppearances': character1 + "," + character2,
    'ts': ts, 
    'apikey': pub,
    'hash': generateHash(ts, priv, pub),
    'orderBy': '-focDate'
  }
  r = requests.get(url+"/comics", params=payload)
  return r.json()

#
#
if __name__ == '__main__':
  # run debugger
  app.run(debug=True)

  # run app
  #app.run()