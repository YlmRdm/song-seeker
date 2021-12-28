from flask import Flask,render_template, redirect, url_for, request,jsonify
app = Flask(__name__)

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
load_dotenv()

import os
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id,client_secret))

@app.route('/',methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		search_text = request.form['search_name']
		results = sp.search(q=search_text, limit=10)
		songlist = results['tracks']['items']
		return render_template('index.html', tracks=songlist)
	else:
		user = request.args.get('search_name')
		return render_template('index.html')

if __name__ == '__main__':
	app.run(debug = True)