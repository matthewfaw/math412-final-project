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
		#else:
		#	return None
	return None

def vectorize_song(song_id):
	client_credentials_manager = SpotifyClientCredentials(client_id=cid.client_id, client_secret=cid.client_secret)
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
	sp.trace=True
	features = sp.audio_features([song_id])
	print json.dumps(features, indent=4)
	dict = features[0]
	return [dict['acousticness'], dict['danceability'], dict['energy'], dict['instrumentalness'], dict['liveness'], dict['speechiness'], dict['valence']]
	#return [dict['energy'], dict['liveness'], dict['tempo'], dict['speechiness'], dict['acousticness'], dict['instrumentalness'], dict['time_signature'], dict['danceability'], dict['key'], dict['duration_ms'], dict['loudness'], dict['valence']]

def spotify_query(song_name, artist_name):
	song_id = get_spotify_id(song_name, artist_name)
	if song_id == None:
                print "song ID not found, skipping this song for:", song_name
                return 'Song Name: ' + song_name + '\nArist Name:' + artist_name
	return vectorize_song(song_id)

# if len(sys.argv) > 2:
	# song_name = sys.argv[1]
	# artist_name = sys.argv[2]
# else:
	# song_name = 'wake me up when september ends'
	# artist_name = 'green day'

#id = get_spotify_id(song_name, artist_name)
print spotify_query('uptown funk', 'Mark Ronson, Bruno Mars')
