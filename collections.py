'''
   Script to read the JSON files and the export the free text fields
'''

import json
import glob

records = {}

objs = glob.glob('*.json')
for obj in objs:
    f = open(obj, 'r')

    data = json.loads(f.read())

    for datum in data['result']['items']:
        #if "Documenting Homes" in datum['parts'][0]['description']:
        #    print (datum["objectNumber"])
        if datum["collectionCategory"] == "Documenting Home":
            if datum["objectNumber"] not in records:
                records[datum["objectNumber"]] = {}
            records[datum["objectNumber"]] = json.dumps({"keys": datum["webKeywords"], "techniques" : datum["techniques"]})
f = open('collections.csv', 'w')
for key, record in records.iteritems():
    rec = json.loads(record)
    f.write(key + ',' + ';'.join(rec["keys"]) + ',' + ';'.join(rec["techniques"]) + "\n")
