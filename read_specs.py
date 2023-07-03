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
    
    # Extract data-file meta data:
    data_file_type = specs[0]['data file type']
    if data_file_type == "text":
        data_file_type = "txt"
    xx_email = specs[0]['xx email']
    brown_email = specs[0]['brown email']
    strict_email = specs[0]['strict email']
    symbols = specs[0]['allowed symbols']
    meta_data = [delimiter, data_file_type, xx_email, brown_email, strict_email, symbols]
    
    # Get the number of parameters
    columns = specs[1]['parameters']
    parameters_count = len(columns)
    print(f"Number of parameters: {parameters_count}\n")


    parameters = {}
    for param in columns:
        parameter_index = param['index']
        parameter_name = param['parameter']
        parameter_type = param['type']
        parameter_required = param['required']
        if parameter_type == "string" or parameter_type == "str":
            parameter_type = str
        elif parameter_type == "num" or parameter_type == "number" or parameter_type == "int":
            parameter_type = int
        elif parameter_type == "date":
            parameter_type = date
        parameter_length = int(param['maxLength'])
        parameters.update({parameter_index:[parameter_name, parameter_type, parameter_length, parameter_required]})
    
    return meta_data, parameters

   