from data_collection.spotify_queries.artists import get_all_track_ids
from data_collection.grammys.csv_helper import deserialize
from serializer.serializer import serialize as pickle
from serializer.serializer import deserialize as depickle
from data_collection.spotify_queries.queries import vectorize_song

def create_catalogs(entries):
    '''
    Input:
    entries -- a list of grammy Entry objects
    Output:
    A dictionary of the form:
        { artist_name: { album_name: [song_ids] } }
    where the keys of the dictionary correspond to all
    artists featured in the entries
    '''
    catalogs = {}
    for entry in entries:
        artist = entry.credits
        print artist
        catalogs[artist] = get_all_track_ids(artist)
        print catalogs[artist]

    return catalogs

def featureize_catalogs(catalogs):
    '''
    Input:
    catalogs -- the object returned from create_catalogs
    Output:
    a catalog, with populated feature vectors
        { artist_name: { album_name: [[song_vector]] } }
    '''
    for artist_name, albums in catalogs.iteritems():
        print artist_name
        print
        for album_name, song_ids in albums.iteritems():
            print album_name
            for index, song_id in enumerate(song_ids):
                print index, song_id
                catalogs[artist_name][album_name][index] = vectorize_song(song_id)
        print

    print 'Done making'
    return catalogs

def get_all_songs(all_catalogs, artist_name):
    artist_catalog = all_catalogs[artist_name]
    songs = []
    for album, song_vecs in artist_catalog.iteritems():
        songs.extend(song_vecs)
    return songs

# Print out what the catalog looks like
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

# catalogs = featureize_catalogs(catalogs)
catalogs = depickle('artists_tracks_from_record_of_the_year_with_song_feature_vectors')
print 'These are all the song feature vectors off of 52nd Street'
print
print catalogs['Billy Joel']['52nd Street']

# Create a catalog
# entries = deserialize('RECORD_OF_THE_YEAR.csv')
# catalogs = create_catalogs(entries)
# pickle(catalogs,'artists')
