import re
from csv_helper import deserialize, serialize

def negative_filter_by_categories(array, categories):
    """
    array: list of Entries
    categories: a list of categories to match
    return: the list of entries with categories not containing a string in the category array
    """
    ret = []
    toAdd = True
    for e in array:
        for c in categories:
            if c in e.category:
                toAdd = False
                break
        if toAdd:
            ret.append(e)
        toAdd = True
    return ret

def filter_by_categories(array, categories):
    """
    array: a list of Entry objects
    categories: a list of string categories, e.g. ['Song Of The Year','Record Of The Year']
    Returns a list of entries with category field in the list of categories
    """
    return [e for e in array if e.category in categories]

def _get_artist_name(credits):
    search_items = [',', ' &', ' (']
    artist_end = len(credits)
    for item in search_items:
        index = credits.find(item)
        if index != -1:
            artist_end = min(index, artist_end)
    return credits[0:artist_end]

def convert_credits_to_names(array):
    """
    array: list of Entry objects
    Returns the list of Entry objects, where the credits field has been
        converted to an array
    """
    for entry in array:
        entry.credits = _get_artist_name(entry.credits)
    return array

x = deserialize('GRAMMIES_NAMES.csv')
xxx = filter_by_categories(x, ['Record Of The Year'])
serialize(xxx, 'RECORD_OF_THE_YEAR.csv')
# x = deserialize('GRAMMIES.csv')
# categories = ['Album','Artist','Producer','Remixer','Video','Package']
# xx = negative_filter_by_categories(x, categories)
# xxx = convert_credits_to_names(xx)
# serialize(xxx,'ALL_SONGS.csv')
