import sys
import spotipy

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
	return

if len(sys.argv) > 2:
	song_name = sys.argv[1]
	artist_name = sys.argv[2]
else:
	song_name = 'wake me up when september ends'
	artist_name = 'green day'

print get_spotify_id(song_name, artist_name)
