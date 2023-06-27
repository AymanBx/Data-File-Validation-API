from read_specs import read_specs

def validate_file(data_file, spec_file):
    delimiter, specs = read_specs(spec_file)
    print("delimiter:", delimiter)
    print()

    extracted = {}
    with open(data_file, 'r') as file:
        data = file.read()
        num = 0
        for line in data.splitlines():
            num += 1
            # print("record:", num)
            extracted.update({num:[]})
            for piece in line.split("|"):
                piece = piece.strip()
                list = extracted.get(num)    
                list.append(piece)
            # print(list)

    # print("data:", data, "\nThanks\n")

    for record in (extracted.values()):
        record_range = len(record)
        if len(specs.keys()) != len(record):
            record_range = len(specs.keys())
        for param in range(record_range):
            if type(record[param]) != specs.get(param)[1]:
                print("Well,", record[param], "failed type test!")
            # else:
                # print("SO,", record[param], "passed type test!")
            if len(record[param]) > specs.get(param)[2]:
                print("Well,", record[param], "failed length test!")
            # else:
                # print("SO,", record[param], "passed length test!")