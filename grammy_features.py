from data_collection.grammys.csv_helper import deserialize
from data_collection.grammys.csv_helper import serialize as csv_serialize
from data_collection.spotify_queries.queries import spotify_query
from  serializer.serializer import serialize

entries_list = []
not_found_songs = []
for entry in deserialize('RECORD_OF_THE_YEAR.csv'):
    feature = spotify_query(entry.nominee_work, entry.credits)
    if isinstance(feature, basestring):
        not_found_songs.append(entry)
        feature = []
    entry.set_feature_vector(feature)
    entries_list.append(entry)

csv_serialize(not_found_songs, 'NOT_FOUND.csv')
csv_serialize(entries_list, "RECORD_OF_THE_YEAR.csv")
for i in not_found_songs:
    print i
print "Number of songs not found: ", len(not_found_songs)
