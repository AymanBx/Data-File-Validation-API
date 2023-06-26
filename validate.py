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
            print("record:", num)
            extracted.update({num:[]})
            for piece in line.split("|"):
                piece = piece.strip()
                list = extracted.get(num)    
                list.append(piece)
            print(list)

    print("data:", data, "\nThanks\n")

    for record in (extracted.values()):
        for param in range(len(record)):
            if type(record[param]) != specs.get(param)[1]:
                print("error!!!")
            else:
                print("SO,", record[param], "passed type test!")
            if len(record[param]) > specs.get(param)[2]:
                print("error2!!!")
            else:
                print("SO,", record[param], "passed length test!")