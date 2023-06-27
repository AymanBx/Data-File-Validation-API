from read_specs import read_specs


def validate_file(data_file, spec_file):
    # Read the spec file
    delimiter, specs = read_specs(spec_file)
    print("delimiter:", delimiter, "\n")
    
    # Read the data file
    data = read_data(data_file)
   
    # Validate data
    # !!! Need to make it more abstract in validating different specs
    print("\n\nIN VALIDATION")
    for record in data:
        print(record)
        print(specs)
        print(f"Spec keys: {specs.keys()}")
        for param in specs.keys():
            print(f"Param(key): {param}")
            if record.get(param) == None or type(record.get(param)) != specs.get(param)[1]:
                print("Well,", record.get(param), "failed type test!")
            # else:
                # print("SO,", record.get(param), "passed type test!")
            if record.get(param) == None or len(record.get(param)) > specs.get(param)[2]:
                print("Well,", record.get(param), "failed length test!")
            # else:
                # print("SO,", record.get(param), "passed length test!")
            print()

                

def read_data(data_file):
    # !!! Might want  to change processed data to a list now (((Done)))
    processed_data = []
    with open(data_file, 'r') as file:
        raw_data = file.read()
    
    record_count = 0
    for line in raw_data.splitlines():
        record_count += 1
        record = {}

        field_index = 0
        for field in line.split("|"):
            field = field.strip()
            field_index += 1
            if field == '' or field == 'N/A':
                continue
            record.update({field_index:field})
        processed_data.append(record)
        print(record)
    
    print(f"Processed {record_count} records")
    return processed_data