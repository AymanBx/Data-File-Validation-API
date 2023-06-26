import json

with open('Maxient Spec.json') as json_file:
    specs = json.load(json_file)


    if specs[0]['fileFormat']['format'] == "delimited records":
        delimiter = specs[0]['fileFormat']['delimiter']
    print("delimiter:", delimiter)
    print()
    if delimiter:
       parameters_count = len(specs[1]['columns'])
       print("Number of parameters:", parameters_count)
       print()

       parameters = []
       for num in range (0,parameters_count):
           parameter_name = specs[1]['columns'][num]['parameter']
           parameter_type = specs[1]['columns'][num]['type']
           parameter_length = specs[1]['columns'][num]['maxLength']
           parameters.append((parameter_name, parameter_type, parameter_length))
           print(parameters[num])

       
    
    else:
        print("I don't know how to with these records yet!")

   