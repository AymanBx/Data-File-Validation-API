import sys
import os
import json
from validate import validate_file

# Usage statment can be printed to user in case of an error in passing arguments
usage_statement = "Usage\n\tmain.py <DataFile Name> <SpecFile Name>\n"

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

if ((not data_file.endswith(".txt")) or (not spec_file.endswith(".json"))):
    print("One of the files' type doesn't meet the specs of this program.")
    exit(0)


# Read data file specs
# delimiter, specs = read_specs(spec_file)
# for spec in specs.values():
#     print(spec)
# print("specs read success\n")

# Validate data
errors = validate_file(data_file, spec_file)
print("Validation complete!\n")

if len(errors.keys()) > 0:
        outformatted_content = ",\n".join(["\t" + json.dumps({k: v}) for k, v in errors.items()])

# Create a new output file
with open("out.json", 'w') as output:
    if outformatted_content:
        output.write("[\n")
        output.write(outformatted_content)
        output.write("\n]")
    print("output file created.")
        
        