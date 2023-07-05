import json
from datetime import date

def read_specs(json_file):
    # Import spec data into a variable   
    with open(json_file) as spec_file:
        specs = json.load(spec_file)

    # Check the format
    if specs[0]['format'] != "delimited records":
        print("I don't know how deal to with these records yet!")
        exit(0)
    
    # Extract data-file meta data:
    delimiter = specs[0]['delimiter']
    data_file_type = specs[0]['data file type']
    if data_file_type == "text":
        data_file_type = "txt"
    primary_key = specs[0]['column_identifier']
    xx_email = specs[0]['xx email']
    brown_email = specs[0]['brown email']
    strict_email = specs[0]['strict email']
    symbols = specs[0]['allowed symbols']
    meta_data = [delimiter, data_file_type, primary_key, xx_email, brown_email, strict_email, symbols]
    
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


def read_data(data_file, delimiter):
    # !!! Might want  to change processed data to a list now (((Done)))
    processed_data = []
    with open(data_file, 'r') as file:
        raw_data = file.read()
    
    record_count = 0
    for line in raw_data.splitlines():
        record_count += 1
        record = {}

        field_index = 0
        for field in line.split(delimiter):
            field = field.strip()
            field_index += 1
            if field == '':
                continue
            elif field == 'n/a':
                field = 'N/A'
            record.update({field_index:field})
        processed_data.append(record)
        # print(record)
    
    print(f"Processed {record_count} records")
    return processed_data
   