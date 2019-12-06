import itertools

def main():
    with open("input.txt") as f:
        instructions = f.read().strip('\n').split(',')
        start_memory = list(map(lambda x: int(x), instructions))
        configs = list(itertools.product(range(0,100), range(0,100)))
        start = True
        for elem in configs:
            pos = 0
            instructions = list(start_memory)
            instructions[1] = elem[0]
            instructions[2] = elem[1]
            while instructions[pos] != 99:
                if instructions[pos] == 1:
                    instructions[instructions[pos+3]] = instructions[instructions[pos+1]] + instructions[instructions[pos+2]]
                elif instructions[pos] == 2:
                    instructions[instructions[pos+3]] = instructions[instructions[pos+1]] * instructions[instructions[pos+2]]
                pos += 4
            start = False
            if instructions[0] == 19690720:
                print(100*elem[0]+elem[1])
                break

if __name__ == "__main__":
    main()
