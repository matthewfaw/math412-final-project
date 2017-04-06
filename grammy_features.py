from data_collection.grammys.csv_helper import deserialize
from spotify_queries.queries import spotify_query
from  serializer.serializer import serialize

entries_list = []
not_found_songs = []
for entry in deserialize('20170405-213931NAMED.csv'):
    feature = spotify_query(entry.nominee_work, entry.credits)
    if isinstance(feature, basestring):
        not_found_songs.append(feature)
    entries_list.append(feature)

serialize(entries_list, "entries")
for i in not_found_songs:
    print i
print "Number of songs not found: ", len(not_found_songs)



