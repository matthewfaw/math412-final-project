import time
import unicodecsv as csv
import os
from grammy_entry import Entry

DEFAULT_FILEPATH = os.path.dirname(__file__) + '/../grammy_data/'

def _defaultify(filename):
    return DEFAULT_FILEPATH + filename

def _uniquify(filename):
    time_str = time.strftime("%Y%m%d-%H%M%S")
    return time_str + filename

def serialize(array, filename):
    """
    Serializes the input array to a CSV file
    Assumes each entry of the array contains a method called toArray()
        the entries of each entry.toArray() will be the entries of each row of the CSV file
    The method converts the filename to a unique string by appending the date to the name,
        then places the file in DEFAULT_FILEPATH directory
    """
    with open(_defaultify(_uniquify(filename)), 'wb') as csvfile:
        entrywriter = csv.writer(csvfile, encoding='utf-8')
        for entry in array:
            entrywriter.writerow(entry.toArray())

def deserialize(filename):
    """
    Deserializes the filename into an array of Grammy Entry objects
    Assumes filename is in the DEFAULT_FILEPATH directory
    """
    entries = []
    with open(_defaultify(filename), 'rb') as csvfile:
        entrywriter = csv.reader(csvfile, encoding='utf-8')
        for row in entrywriter:
            entry = Entry(row[0], row[1], row[2], row[3])
            entries.append(entry)
    return entries

# arr = []
# e = Entry('2015','best of the year', 'nothing', 'no one')
# arr.append(e)
# arr.append(e)
# arr.append(e)
# serialize(arr,'derp.csv')
# deserialize('derp.csv')
