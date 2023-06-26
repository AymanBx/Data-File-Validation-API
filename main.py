import sys
import os

# Usage statment can be printed to user in case of an error in passing arguments
usage_statement = "Usage\n\tmain.py <DataFile Name> <SpecFile Name>\n"


# Read filenames from stdin
arguments = sys.argv

print("files:", len(arguments)-1)
print()

# Check that the correct number of arguments was provided
if len(arguments) != 3:
    print(usage_statement)
    exit(0)

# Take in file names
data_file = arguments[1]
print("data file:", data_file)
spec_file = arguments[2]
print("spec file:", spec_file, "\n")

if (not os.path.exists(data_file)) or (not os.path.exists(spec_file)) :
    print("One of the files doesn't exist----hint: could be a typo in the file name.")
    exit(0)
# else:
#     print("Check!")