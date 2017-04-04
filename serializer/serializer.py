import json


def serialize(data, string_id):
  with open('./data/'+ string_id + '.json', 'w') as open_file:
    json.dump(data, open_file)


def deserialize(string_id):
  with open('./data/' + string_id + '.json', 'r') as open_file:
    return json.load(open_file)
