import json

with open('Maxient Spec.json') as json_file:
    specs = json.load(json_file)

    print(specs[0]['fileFormat']['format'])
    print()

    print(len(specs[1]['columns'][0]))

   