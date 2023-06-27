import json
from datetime import date

def read_specs(json_file):
    # Import spec data into a variable   
    with open(json_file) as spec_file:
        specs = json.load(spec_file)

    # Check the format
    if specs[0]['format'] == "delimited records":
        delimiter = specs[0]['delimiter']
    else:
        print("I don't know how deal to with these records yet!")
        exit(0)
    
    # Get the number of parameters
    columns = specs[1]['parameters']
    parameters_count = len(columns)
    print("Number of parameters:", parameters_count)
    print()

    parameters = {}
    for num in range (0,parameters_count):
        parameter_name = columns[num]['parameter']
        parameter_type = columns[num]['type']
        if parameter_type == "string" or parameter_type == "str":
            parameter_type = str
        elif parameter_type == "num" or parameter_type == "number" or parameter_type == "int":
            parameter_type = int
        elif parameter_type == "date":
            parameter_type = date
        parameter_length = int(columns[num]['maxLength'])
        parameters.update({num:[parameter_name, parameter_type, parameter_length]})
    
    return delimiter, parameters

   