
with open("input.txt") as f:
    instructions = f.read().strip('\n').split(',')
    instructions = list(map(lambda x: int(x), instructions))
    instructions[1] = 12
    instructions[2] = 2
    pos = ]0
    while instructions[pos] != 99:
        if instructions[pos] == 1:
            instructions[instructions[pos+3]] = instructions[instructions[pos+1]] + instructions[instructions[pos+2]]
        elif instructions[pos] == 2:
            instructions[instructions[pos+3]] = instructions[instructions[pos+1]] * instructions[instructions[pos+2]]
        pos += 4
    print(instructions[0])
