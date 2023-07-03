import sys
import os
import json
from read_files import read_specs
from read_files import read_data
from validate import validate_file

# Usage statment can be printed to user in case of an error in passing arguments
usage_statement = "Usage\n\tmain.py <DataFile Name>.txt(or.csv) <SpecFile Name>.json\n"

# Check that the correct number of arguments was provided
if len(sys.argv) != 3:
    print(usage_statement)
    exit(0)

# Read filenames from stdin arguments 
data_file = sys.argv[1]
spec_file = sys.argv[2]

# print("files:", len(sys.argv)-1)
print(f"data file: {data_file}")
print(f"spec file: {spec_file}\n")
 

# Check that input files exist and are of the correct types
if (not os.path.exists(data_file)) or (not os.path.exists(spec_file)) :
    print("One of the files doesn't exist----hint: could be a typo in the file name.")
    exit(0)

if not spec_file.endswith(".json"):
    print("Spec file needs to be a json file.\n\n", usage_statement)
    exit(0)

# Read the spec file
meta_data, specs = read_specs(spec_file)
delimiter = meta_data[0]
data_file_type = meta_data[1]
print("delimiter:", delimiter, "\n")

if not data_file.endswith(f".{data_file_type}"):
    print(f"Data file needs to be a {data_file_type} file.\n\n{usage_statement}")
    exit(0)

# Read the data file
data = read_data(data_file, delimiter)

# Validate data
errors = validate_file(meta_data, specs, data)
print("Validation complete!\n")

if len(errors.keys()) > 0:
        outformatted_content = ",\n".join(["\t" + json.dumps({k: v}) for k, v in errors.items()])

# Create a new output file
with open("out.json", 'w') as output:
    if len(errors.keys()) > 0:
        output.write("[\n")
        output.write(outformatted_content)
        output.write("\n]")
    print("output file created.")
        
        