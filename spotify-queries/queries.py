from ids import client_ids as cid
from spotipy.oauth2 import SpotifyClientCredentials
import json
import sys
import spotipy
import time

sp = spotipy.Spotify()

def get_spotify_id(song_name, artist_name):
	results = sp.search(q=song_name)
	for track in results['tracks']['items']:
		#print track['artists'][0]['name']
		#print track['id']
		if track['artists'][0]['name'].lower() == artist_name.lower():
			return track['id']
		else:
			return None

def vectorize_song(song_id):
	print cid.client_id
	print cid.client_secret
	client_credentials_manager = SpotifyClientCredentials(client_id=cid.client_id, client_secret=cid.client_secret)
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
	sp.trace=True
	start = time.time()
	features = sp.audio_features([song_id])
	delta = time.time() - start
	print(json.dumps(features, indent=4))
	print ("features retrieved in %.2f seconds" % (delta,))
	return

if len(sys.argv) > 2:
	song_name = sys.argv[1]
	artist_name = sys.argv[2]
else:
	song_name = 'wake me up when september ends'
	artist_name = 'green day'

id = get_spotify_id(song_name, artist_name)
print id
vectorize_song(id) 
