from read_specs import read_specs
from datetime import datetime, date

date_format = "%Y-%m-%d"
errors = {}

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
            errors.update({keyVar: "Doesn't have a Brown ID!"})
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
                    errors.update({keyVar: f"{check_name} value isn't all digits."})
            elif check_type == "lInt":
                for char in field:
                    if not char.isdigit() and char != '-':
                        errors.update({keyVar: f"{check_name} value can only have digits or dashes in it."})
            elif check_type == date:
                try:
                    datetime.strptime(field, date_format)
                except ValueError:
                    errors.update({keyVar: f"{check_name} value is not in correct date format."})
            elif check_type == str:
                try:
                    int(field)
                    errors.update({keyVar: f"{check_name} value needs to have letters in it."})
                except ValueError:
                    True      
            elif check_type == "sString":
                if any(char.isdigit() for char in field):
                    errors.update({keyVar: f"{check_name} value can't have digits in it."})
            elif check_type == "email":
                if not field.endswith("@brown.edu") and not field.endswith("@brown.eduxx") and not field.endswith("brown.edu"):
                    errors.update({keyVar: f"{check_name} value not a valild Brrown email."})
                else:
                    for char in field:
                        if not char.isalpha() and not char.isdigit() and char != '+' and char != '_' and char != '-' and char != '.' and char != '@':
                            errors.update({keyVar: f"{check_name} value emails can't have weird symbols in them."})
            # else:
                # print("SO,", record.get(param), "passed type test!")

            
            # Length check
            if len(str(field)) > check_len:
                errors.update({keyVar: f"{check_name} value has failed the length test!"})
            # else:
                # print("SO,", record.get(param), "passed length test!")

    return errors

                

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