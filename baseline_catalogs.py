from serializer.serializer import serialize as pickle
from serializer.serializer import deserialize as depickle
from artist_catalogs import create_catalogs, featureize_catalogs
from data_collection.grammys.grammy_entry import Entry

def _create_entries(artist_list=[]):
    entries = []
    for artist in artist_list:
        entries.append(Entry('','','',artist))
    return entries

def create_populated_artist_catalog(artist_list, output_filename):
    entries = _create_entries(artist_list)
    catalogs = create_catalogs(entries)
    catalogs_vec = featureize_catalogs(catalogs)
    pickle(catalogs_vec,output_filename)

baseline_artists = [
        'R.E.M.',
        'The Police',
        'Derek & The Dominos',
        'Buddy Guy',
        'Keane',
        'Snow Patrol',
        ]

# catalogs = create_populated_artist_catalog(baseline_artists, 'baseline_artists_populated_feature_vectors')
