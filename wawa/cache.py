import json

def save(tuples, filename):
    out_filename = filename[:-4] + ".json"
    print(out_filename)
    with open(out_filename, "w") as output:
        json.dump(tuples, output)

def open(file):
    tuples = json.load(file)
    return tuples
