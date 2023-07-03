from read_specs import read_specs
from datetime import datetime, date

date_format = "%Y-%m-%d"
errors = {}

def validate_file(meta_data, specs, data): 
    # Validate data
    # !!! Need to make it more abstract in validating different specs
    print("\n\nIN VALIDATION")

    xx_email = meta_data[2]
    brown_email = meta_data[3]
    strict_email = meta_data[4]
    symbols = meta_data[5]
    for num, record in enumerate(data):
        # print(record)
        # Get the brown ID and check it exists
        keyVar = record.get(1)
        if keyVar == None:
            keyVar = f"#{num}"
            errors.update({f"#{num}": f"Record #{num} is missing primary key."})
            # continue


        for param in specs.keys():
            # Get the data value to be validated
            field :str = record.get(param)
            
            # Get the checks for this field
            check_name = specs.get(param)[0]
            check_type = specs.get(param)[1]
            check_len = specs.get(param)[2]
            required = specs.get(param)[3]

            # Skip empty not required fields
            if field == None and not required:
                continue
            elif field == None:
                errors.update({keyVar: f"{check_name} must have a value or N/A."})
                continue
            # elif field == "N/A" and check_name == "athleticMember":
            #     errors.update({keyVar: f"{check_name} muZZZZZZZZZZZZZZZ"})
            

            # Cleaning data up
            # Remove dash from zip code
            if check_type == "zip":
                field = field.replace("-", "", 1)
            # All fields to lowercase
            if not check_type == "gender":
                field = field.lower()
            # Emails stripped from "xx"
            if check_type == "email" and xx_email and field.startswith("xx") and field.endswith("xx"):
                field = field.rstrip("xx")
                field = field.replace("xx", "", 1)
            # Remove @ from email
            if check_type == "email":
                field = field.replace("@", "", 1)


            # Type tests:
            # Check: int values don't have anything other that digits
            if check_type == int or check_type == "zip":
                try:
                    int(field)
                except ValueError:
                    errors.update({keyVar: f"{check_name} value isn't all digits."})

            # Check: date value is in correct format
            elif check_type == date:
                try:
                    datetime.strptime(field, date_format)
                except ValueError:
                    errors.update({keyVar: f"{check_name} value is not in correct date format."})
            
            # Check: string variable isn't all digits
            elif check_type == str and check_type == "email":
                try:
                    int(field)
                    errors.update({keyVar: f"{check_name} value can't be all digits."})
                except ValueError:
                    True      
            
            # Check: strict strings don't have digits or weird symbols in them
            elif check_type == "sString":
                if any((char.isdigit() or char =='$') for char in field):
                    errors.update({keyVar: f"{check_name} value can't have digits in it."})
            
            # Check: emails are valid - brown/non-brown emails
            if check_type == "email":
                if  not xx_email and field.startswith("xx") and field.endswith("xx"):
                    errors.update({keyVar: f"{check_name} must be a valid email."})
                if brown_email and not field.endswith("brown.edu"):
                    errors.update({keyVar: f"{check_name} value must be a valid Brown email."})
                for char in field:
                    if strict_email and not char.isalpha() and not char.isdigit():
                        errors.update({keyVar: f"{check_name} value can't have weird symbols in it."})
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
            if field == '':
                continue
            elif field == 'n/a':
                field = 'N/A'
            record.update({field_index:field})
        processed_data.append(record)
        # print(record)
    
    print(f"Processed {record_count} records")
    return processed_data