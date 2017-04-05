import csv
from grammy_entry import Entry

def serialize(array, filename):
    with open(filename, 'wb') as csvfile:
        entrywriter = csv.writer(csvfile)
        for entry in array:
            entrywriter.writerow(entry.toArray())

def deserialize(filename):
    entries = []
    with open(filename, 'rb') as csvfile:
        entrywriter = csv.reader(csvfile)
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
