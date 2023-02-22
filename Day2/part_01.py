def pre_run(intcode):
    intcode[1] = 12
    intcode[2] = 2

    return intcode

def process_intcode(intcode):
    """Processes an intcode based on the opcode"""
    for i in range(0, len(intcode), 4):
        if i + 3 >= len(intcode):
            break

        x = intcode[intcode[i + 1]]
        y = intcode[intcode[i + 2]]
        z = intcode[i + 3]

        if intcode[i] == 1:
            intcode[z] = x + y

        elif intcode[i] == 2:
            intcode[z] = x * y

        elif intcode[i] == 99:
            break

    return intcode

if __name__ == '__main__':
    with open("input") as file:
        data = file.read()
    intcode_data = data.split(',')
    intcode_data = list(map(int, intcode_data))
    results = process_intcode(pre_run(intcode_data))
    print(results[0])