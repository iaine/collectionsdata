'''
   Script to import json
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
        if datum['objectNumber'].startswith("?"):
            if datum["objectNumber"] not in records:
                records[datum["objectNumber"]] = {}
            records[datum["objectNumber"]] = json.dumps(datum["webKeywords"])

for record in records.iteritems():
    print(record)
