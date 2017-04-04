import pickle


def serialize(data, string_id):
  with open('./data/'+ string_id + '.json', 'w') as open_file:
    pickle.dump(data, open_file)


def deserialize(string_id):
  with open('./data/' + string_id + '.json', 'r') as open_file:
    return pickle.load(open_file)
