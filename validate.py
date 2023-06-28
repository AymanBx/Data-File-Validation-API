from read_specs import read_specs
from datetime import datetime, date

date_format = "%Y-%m-%d"

def validate_file(data_file, spec_file):
    # Read the spec file
    delimiter, specs = read_specs(spec_file)
    print("delimiter:", delimiter, "\n")
    
    # Read the data file
    data = read_data(data_file, delimiter)
   
    # Validate data
    # !!! Need to make it more abstract in validating different specs
    print("\n\nIN VALIDATION")
    for record in data:
        # print(record)
        # Get the brown ID and check it exists
        keyVar = record.get(1)
        if keyVar == None:
            print(f"Record number {data.index(record)}, doesn't have a Brown ID!")
            continue


        for param in specs.keys():
            # Get the data value to be validated
            field = record.get(param)
            if field == None:
                continue

            # Get the checks for this field
            check_name = specs.get(param)[0]
            check_type = specs.get(param)[1]
            check_len = specs.get(param)[2]

            # Type check
            if check_type == int:
                try:
                    int(field)
                except ValueError:
                    print(f"{check_name} value for record {keyVar} failed type test!")
            elif check_type == date:
                try:
                    datetime.strptime(field, date_format)
                except ValueError:
                    print(f"{check_name} value for record {keyVar} failed type test!")
            # elif check_type == str:
            #     if any(char.isdigit() for char in field):
            #         print(f"{check_name} value for record {keyVar} has digits in it!")             
            # else:
                # print("SO,", record.get(param), "passed type test!")

            
            # Length check
            if len(str(field)) > check_len:
                print(f"{check_name} value for record {keyVar} has failed the length test!")    
            # else:
                # print("SO,", record.get(param), "passed length test!")

                

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
            if field == '' or field == 'N/A':
                continue
            record.update({field_index:field})
        processed_data.append(record)
        # print(record)
    
    print(f"Processed {record_count} records")
    return processed_data