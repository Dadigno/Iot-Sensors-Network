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


def update_resource(root, rawJson):
    data = json.loads(rawJson)

    with open(filepath, 'r') as f:
        res = json.load(f)

    k = list(data.keys())
    res[root][k[0]] = data[str(k[0])]
    with open(filepath, 'w') as fp:
        json.dump(res, fp, indent=2)



