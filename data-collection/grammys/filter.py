from csv_helper import deserialize, serialize

def filter_by_category(array, category):
    return [e for e in array if e.category == category]

x = deserialize('GRAMMIES.csv')
xf = filter_by_category(x, 'Song Of The Year')
serialize(xf,'FILTERED.csv')

e = xf[0]
print e.year
