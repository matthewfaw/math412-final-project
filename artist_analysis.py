from serializer.serializer import deserialize as depickle
import numpy as np
import matplotlib.pyplot as plt
import data_analysis.do_pca as pca
import rips
from artist_catalogs import get_all_songs

catalogs = depickle('artists_tracks_from_record_of_the_year_with_song_feature_vectors')
base_catalogs = depickle('baseline_artists_populated_feature_vectors')

def analyze_artists(catalog, persistence_dim, clean_data_fcn, plot_fcn, save_plot):
    '''
    Input:
    catalog: a catalog of multiple artists, with populated feature vectors
        { artist_name: { album_name: [[song_vector]] } }
    persistence_dim: an integer that specifies which dimension of persistence to produce
    clean_data_fcn: a lambda that prepares data for plotting
    plot_fcn: a lambda to plot the data
    save_plot: a boolean specifying whether or not to save the plot
    Output:
    persistence diagram for each of the artist's albums
    '''
    for artist, artist_catalog in catalog.iteritems():
        analyze_artist(artist, artist_catalog, persistence_dim, clean_data_fcn, plot_fcn, save_plot)

def analyze_artist(artist, artist_dict, persistence_dim, clean_data_fcn, plot_fcn, save_plot):
    '''
    Input:
    artist_dict: a catalog, with populated feature vectors
        { album_name: [[song_vector]] }
    persistence_dim: an integer that specifies which dimension of persistence to produce
    clean_data_fcn: a lambda that prepares data for plotting
    plot_fcn: a lambda to plot the data
    save_plot: a boolean specifying whether or not to save the plot
    Output:
    persistence diagram for the artist's albums
    '''
    short_albums = []
    for album, song_vectors in artist_dict.iteritems():
        if len(song_vectors) > persistence_dim + 1:
            vector_array = np.array(song_vectors)
            cleaned_vector = clean_data_fcn(vector_array)
            plot_fcn(cleaned_vector, persistence_dim, artist, album, len(cleaned_vector), clean_data_fcn.__name__, save_plot)
        else:
            print artist, album + " has too few songs"
            short_albums.append(artist + " " + album)
    #print short_albums

def analyze_artist_full(artist, song_vectors, persistence_dim, clean_data_fcn, plot_fcn, save_plot):
    vector_array = np.array(song_vectors)
    cleaned_vector = clean_data_fcn(vector_array)
    plot_fcn(cleaned_vector, persistence_dim, artist, len(cleaned_vector), clean_data_fcn.__name__, save_plot)


def _remove_null(vectors):
    return np.array([list(row) for row in vectors if (row is not None and all(None is not x for x in row))])

def PCA(array):
    cleaned_vectors = _remove_null(array)
    pca_vector_array = pca.do_pca(cleaned_vectors)
    return pca_vector_array

def NO_PCA(array):
    return  _remove_null(array)

def _get_title(artist, album, num_songs, clean_strategy, persistence_dim):
    return ('%s, %s, %s, %dD-persistence\nNumber of Songs: %d' % (artist,album,clean_strategy,persistence_dim, num_songs)).replace('/', '')

def _persistence_plotter(vector, persistence_dim, artist, album, num_songs, clean_strategy, save_plot):
    print vector, persistence_dim
    pca_bd_pairs = rips.one_tda(vector, persistence_dim)
    rips.plotDGM(pca_bd_pairs)
    title = _get_title(artist, album, num_songs, clean_strategy, persistence_dim)
    print title
    plt.title(title)
    if save_plot:
        plt.savefig('./plots/%s.pdf'%title,bbox_inches='tight')
    else:
        print album
        plt.show()
    plt.gcf().clear()

def _no_album_plotter(vector, persistence_dim, artist, num_songs, clean_strategy, save_plot):
    print vector, persistence_dim
    pca_bd_pairs = rips.one_tda(vector, persistence_dim)
    rips.plotDGM(pca_bd_pairs)
    title = _get_title(artist, "", num_songs, clean_strategy, persistence_dim)
    print title
    plt.title(title)
    if save_plot:
        plt.savefig('./plots/%s.pdf'%title,bbox_inches='tight')
    else:
        print album
        plt.show()
    plt.gcf().clear()


print catalogs.keys()

for dim in range(3):
    for clean_fnc in [PCA, NO_PCA]:
        for artist in ["Eric Clapton", "Coldplay", "U2"]:
            analyze_artist(artist, catalogs[artist], dim, clean_fnc, _persistence_plotter, True)
            analyze_artist_full(artist, get_all_songs(catalogs, artist), dim, clean_fnc, _no_album_plotter, True)
        for artist in base_catalogs.keys():
            analyze_artist(artist, base_catalogs[artist], dim, clean_fnc, _persistence_plotter, True)
            analyze_artist_full(artist, get_all_songs(base_catalogs, artist), dim, clean_fnc, _no_album_plotter, True)
#analyze_artists(catalogs, 0, PCA, _persistence_plotter,False)
