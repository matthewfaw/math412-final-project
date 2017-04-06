import time
import unicodecsv as csv
from grammy_entry import Entry

DEFAULT_FILEPATH = 'data/'

def _defaultify(filename):
    return DEFAULT_FILEPATH + filename

def _uniquify(filename):
    time_str = time.strftime("%Y%m%d-%H%M%S")
    return time_str + filename

def serialize(array, filename):
    with open(_defaultify(_uniquify(filename)), 'wb') as csvfile:
        entrywriter = csv.writer(csvfile, encoding='utf-8')
        for entry in array:
            entrywriter.writerow(entry.toArray())

def deserialize(filename):
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
