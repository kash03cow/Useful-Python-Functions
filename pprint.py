#1) pretty print
# speciality :- debugging in console when unstructured data is given.
import pprint
import json
with open("load.json", "r") as f:
    data = json.load(f)
pprint(data)
