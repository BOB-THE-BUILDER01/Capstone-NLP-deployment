import json

test = {"Test" : 1}
jsonstring = json.dumps(test)
print(json.loads(jsonstring)['Test'])