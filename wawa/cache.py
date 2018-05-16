import json

def save_json(tuples, filename):
    out_filename = filename[:-4] + ".json"
    print(out_filename)
    with open(out_filename, 'w') as output:
        json.dump(tuples, output)

def load_json(file):
    tuples = json.load(file)
    return tuples
