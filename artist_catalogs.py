from data_collection.spotify_queries.artists import get_all_track_ids
from data_collection.grammys.csv_helper import deserialize
from serializer.serializer import serialize 
from serializer.serializer import deserialize as depickle

def create_catalogs(csv_file_src):
    entries = deserialize(csv_file_src)

    catalogs = {}
    for entry in entries:
        artist = entry.credits
        print artist
        catalogs[artist] = get_all_track_ids(artist)
        print catalogs[artist]

    return catalogs

catalogs = depickle('artists_tracks_from_record_of_the_year')
print 'These are all the artists who won Record of The Year'
print
print catalogs.keys()
print
print 'These are all of Billy Joel\'s albums'
print
print catalogs['Billy Joel'].keys()
print
print 'These are all the song ids off of 52nd Street'
print
print catalogs['Billy Joel']['52nd Street']

# catalogs = create_catalogs('RECORD_OF_THE_YEAR.csv')
# serialize(catalogs,'artists.json')
