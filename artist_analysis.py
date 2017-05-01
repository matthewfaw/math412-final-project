from serializer.serializer import deserialize as depickle
import numpy as np
import matplotlib.pyplot as plt
import data_analysis.do_pca as pca
import rips

catalogs = depickle('artists_tracks_from_record_of_the_year_with_song_feature_vectors')

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
    for album, song_vectors in artist_dict.iteritems():
        vector_array = np.array(song_vectors)
        cleaned_vector = clean_data_fcn(vector_array)
        plot_fcn(cleaned_vector,persistence_dim, artist, album, clean_data_fcn.__name__, save_plot)

def _remove_null(vectors):
    return np.array([list(row) for row in vectors if (row is not None and all(None is not x for x in row))])

def _pca_data_cleaner(array):
    cleaned_vectors = _remove_null(array)
    pca_vector_array = pca.do_pca(cleaned_vectors)
    return pca_vector_array

def get_title(artist, album, clean_strategy, persistence_dim):
    return '%s, %s, %s, %dD-persistence' % (artist,album,clean_strategy,persistence_dim)

def persistence_plotter(vector, persistence_dim, artist, album, clean_strategy, save_plot):
    print vector, persistence_dim
    pca_bd_pairs = rips.one_tda(vector, persistence_dim)
    rips.plotDGM(pca_bd_pairs)
    title = get_title(artist, album, clean_strategy, persistence_dim)
    print title
    plt.title(title)
    if save_plot:
        plt.savefig('%s.pdf'%title,bbox_inches='tight')
    # else:
        # plt.show()

analyze_artists(catalogs, 0, _pca_data_cleaner, persistence_plotter,False)
