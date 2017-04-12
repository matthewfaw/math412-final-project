from data_collection.grammys.csv_helper import serialize, deserialize

def generate_counts(array):
    category_counts = {}
    for entry in array:
        if entry.category in category_counts:
            category_counts[entry.category] += 1
        else:
            category_counts[entry.category] = 1
    return category_counts

all_grammies = deserialize('GRAMMIES.csv')
not_found=deserialize('NOT_FOUND.csv')

all_counts = generate_counts(all_grammies)
not_found_counts = generate_counts(not_found)

proportion_counts = {}
for entry in all_counts:
    proportion_counts[entry] = float(not_found_counts.get(entry,0))/float(all_counts[entry]) 

print 'CATEGORY: proportion, # not found / total #'
for key in sorted(proportion_counts, key=proportion_counts.get):
    print key,': ', proportion_counts[key], ',', not_found_counts.get(key,0), '/', all_counts[key]

