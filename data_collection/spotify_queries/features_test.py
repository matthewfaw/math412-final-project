# shows acoustic features for tracks for the given artist

from __future__ import print_function    # (at top of module)
from ids import client_ids as cid
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy
import time
import sys

id = cid.client_id
secret = cid.client_secret
print(id)
print(secret)
client_credentials_manager = SpotifyClientCredentials(client_id=id, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=True

if len(sys.argv) > 1:
    tids = sys.argv[1:]
else:
    tids = '3ZffCQKLFLUvYM59XKLbVm'

print(tids)

start = time.time()
features = sp.audio_features(tids)
delta = time.time() - start
print(json.dumps(features, indent=4))
print ("features retrieved in %.2f seconds" % (delta,))
