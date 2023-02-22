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

def find_Noun_verb(intcode, targetOutputt):
    result = 0
    for noun in range(100):
        for verb in range(100):
            intcode[1] = noun
            intcode[2] = verb
            output = process_intcode(intcode)

            if output[0] == targetOutputt:
                result = 100 * noun + verb
                break

        if output[0] == targetOutputt:
            break

    return result