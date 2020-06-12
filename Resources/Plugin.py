###
#Il plugin legge e scrive nel file delle risorse
#json.loads take a string as input and returns a dictionary as output.
#json.dumps take a dictionary as input and returns a string as output.
###
import json

filepath = "../Resources/resources.json"

def read_resources():
    with open(filepath, 'r') as f:
        res = f.read()
    return res


def update_resource(resource, rawJson):
    with open(filepath, 'r') as f:
        res = json.load(f)
    data = json.loads(rawJson)
    res[resource[0]][resource[1]] = data
    with open(filepath, 'w') as fp:
        json.dump(res, fp, indent=2)

