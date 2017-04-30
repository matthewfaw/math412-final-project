from serializer.serializer import deserialize as depickle
import numpy as np
import matplotlib.pyplot as plt
import data_analysis.do_pca as pca
import rips

catalogs = depickle('artists_tracks_from_record_of_the_year_with_song_feature_vectors')

def analyze_artist(artist_dict, persistence_dim):
    '''
    Input:
    a catalog, with populated feature vectors
        { artist_name: { album_name: [[song_vector]] } }
    an integer that specifies which dimension of persistence to produce
    Output:
    persistence diagram for each of the artist's albums
    '''
    for album, song_vectors in artist_dict.iteritems():

        vector_array = np.array(song_vectors)
        cleaned_vectors = remove_null(vector_array)

        pca_vector_array = pca.do_pca(cleaned_vectors)
        pca_bd_pairs = rips.one_tda(pca_vector_array, persistence_dim)

        rips.plotDGM(pca_bd_pairs)
        plt.show()

def remove_null(vectors):
    return np.array([list(row) for row in vectors if (row is not None and all(None is not x for x in row))])

analyze_artist(catalogs['Billy Joel'], 0)
