from data_collection.grammys.csv_helper import serialize, deserialize

x=deserialize('NOT_FOUND.csv')
a = {}
for e in x:
    if e.category in a:
        a[e.category] += 1
    else:
        a[e.category] = 1

for key in sorted(a, key=a.get):
    print key,': ', a[key]

