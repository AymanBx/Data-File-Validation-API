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
                    print(f"{check_name} value for record {keyVar} isn't all digits.")
            elif check_type == "lInt":
                for char in field:
                    if not char.isdigit() and char != '-':
                        print(f"{check_name} value for record {keyVar} can only have digits or dashes in it.")
            elif check_type == date:
                try:
                    datetime.strptime(field, date_format)
                except ValueError:
                    print(f"{check_name} value for record {keyVar} is not in correct date format.")
            elif check_type == str:
                try:
                    int(field)
                    print(f"{check_name} value for record {keyVar} needs to have letters in it.")
                except ValueError:
                    True      
            elif check_type == "sString":
                if any(char.isdigit() for char in field):
                    print(f"{check_name} value for record {keyVar} can't have digits in it.")
            elif check_type == "email":
                if not field.endswith("@brown.edu") and not field.endswith("@brown.eduxx") and not field.endswith("brown.edu"):
                    print(f"{check_name} value for record {keyVar} not a valild Brrown email.")
                else:
                    for char in field:
                        if not char.isalpha() and not char.isdigit() and char != '+' and char != '_' and char != '-' and char != '.' and char != '@':
                            print(f"{check_name} value for record {keyVar} emails can't have weird symbols in them.")
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
            record.update({field_index:field.lower()})
        processed_data.append(record)
        # print(record)
    
    print(f"Processed {record_count} records")
    return processed_data