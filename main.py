import sys

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
