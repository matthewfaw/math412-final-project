from ids import client_ids as cid
from spotipy.oauth2 import SpotifyClientCredentials
import json
import sys
import spotipy

client_credentials_manager = SpotifyClientCredentials(client_id=cid.client_id, client_secret=cid.client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def _get_artist_info(artist_name):
    '''
    Returns the spotify artist object
    Note that this method returns the first search result
    '''
    results = sp.search(q=artist_name, limit=1,type='artist')
    artist = results['artists']['items'][0]
    return artist

def _get_albums(artist_name):
    '''
    Returns all spotify album objects corresponding to the
    artist artist_name
    '''
    artist_id = _get_artist_info(artist_name)['id']
    albums = sp.artist_albums(artist_id)['items']
    return [a for a in albums if 'US' in a['available_markets']]

def _get_track_ids(album_id):
    '''
    Returns the song ids for each song on the album corresponding
    to spotify id album_id
    '''
    tracks = sp.album_tracks(album_id)['items']
    return [t['id'] for t in tracks]

def convert_map_vals_to_list(m):
    '''
    Accumulates all track ids into a single list, given the
    output of get_all_track_ids
    '''
    y = []
    [y.extend(v) for v in m.values()]
    return y
    

def get_all_track_ids(artist_name):
    '''
    Returns a dictionary in the following format:
        {AlbumName: [song_id]}
    '''
    tracks = {}
    for album in _get_albums(artist_name):
        print album['name']
        print album['album_type']
        tracks[album['name']] = _get_track_ids(album['id'])
    return tracks

m = {}
if len(sys.argv) == 2:
    m = get_all_track_ids(sys.argv[1])
    print m
# else:
    # m= get_all_track_ids('Arcade Fire')
# print convert_map_vals_to_list(m)
