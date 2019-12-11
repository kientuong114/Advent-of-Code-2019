import sys

def main():
    with open("input.txt") as f:
        instructions = f.read().strip('\n').split(',')
        start_memory = list(map(lambda x: x, instructions))
        start = True
        pos = 0
        instructions = list(start_memory) + ['0' for _ in range(150)]
        relative_base = 0
        while instructions[pos][-2:] != "99":
            n_params = len(instructions[pos]) - 2
            param_list = [0,0,0]
            op_list = [0,0,0]

            for i in range(n_params):
                param_list[i] = instructions[pos][-3-i]

            param_list = list(map(lambda x: int(x), param_list))

            #for index,elem in enumerate(instructions):
                #Jsys.stdout.write("["+str(index)+"] "+str(elem)+", ")


            if int(instructions[pos][-2:]) == 1:
                for i in range(3):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    elif param_list[i] == 1:
                        op_list[i] = pos+1+i
                    elif param_list[i] == 2:
                        op_list[i] = relative_base + int(instructions[pos+1+i])

                op_list = list(map(lambda x: int(x), op_list))
                
                instructions[op_list[2]] = str(int(instructions[op_list[0]]) + int(instructions[op_list[1]]))
                pos += 4
                    
            elif int(instructions[pos][-2:]) == 2:
                for i in range(3):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    elif param_list[i] == 1:
                        op_list[i] = pos+1+i
                    elif param_list[i] == 2:
                        op_list[i] = relative_base + int(instructions[pos+1+i])
                op_list = list(map(lambda x: int(x), op_list))

                instructions[op_list[2]] = str(int(instructions[op_list[0]]) * int(instructions[op_list[1]]))
                pos += 4

            elif int(instructions[pos][-2:]) == 3:
                for i in range(1):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    elif param_list[i] == 1:
                        op_list[i] = pos+1+i
                    elif param_list[i] == 2:
                        op_list[i] = relative_base + int(instructions[pos+1+i])
                op_list = list(map(lambda x: int(x), op_list))
                val = 2
                instructions[op_list[0]] = str(val)
                pos += 2

            elif int(instructions[pos][-2:]) == 4:
                for i in range(1):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    elif param_list[i] == 1:
                        op_list[i] = pos+1+i
                    elif param_list[i] == 2:
                        op_list[i] = relative_base + int(instructions[pos+1+i])
                op_list = list(map(lambda x: int(x), op_list))
                print("output: "+str(instructions[op_list[0]]))
                pos += 2

            elif int(instructions[pos][-2:]) == 5:
                for i in range(2):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    elif param_list[i] == 1:
                        op_list[i] = pos+1+i
                    elif param_list[i] == 2:
                        op_list[i] = relative_base + int(instructions[pos+1+i])
                op_list = list(map(lambda x: int(x), op_list))
                if int(instructions[op_list[0]]) != 0:
                    pos = int(instructions[op_list[1]])
                else: 
                    pos += 3
            elif int(instructions[pos][-2:]) == 6:
                for i in range(2):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    elif param_list[i] == 1:
                        op_list[i] = pos+1+i
                    elif param_list[i] == 2:
                        op_list[i] = relative_base + int(instructions[pos+1+i])
                op_list = list(map(lambda x: int(x), op_list))
                if int(instructions[op_list[0]]) == 0:
                    pos = int(instructions[op_list[1]])
                else: 
                    pos += 3
            elif int(instructions[pos][-2:]) == 7:
                for i in range(3):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    elif param_list[i] == 1:
                        op_list[i] = pos+1+i
                    elif param_list[i] == 2:
                        op_list[i] = relative_base + int(instructions[pos+1+i])
                op_list = list(map(lambda x: int(x), op_list))
                if int(instructions[op_list[0]]) < int(instructions[op_list[1]]):
                    instructions[op_list[2]] = 1
                else:
                    instructions[op_list[2]] = 0

                pos += 4

            elif int(instructions[pos][-2:]) == 8:
                for i in range(3):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    elif param_list[i] == 1:
                        op_list[i] = pos+1+i
                    elif param_list[i] == 2:
                        op_list[i] = relative_base + int(instructions[pos+1+i])
                op_list = list(map(lambda x: int(x), op_list))

                if int(instructions[op_list[0]]) == int(instructions[op_list[1]]):

                    instructions[op_list[2]] = 1
                else:
                    instructions[op_list[2]] = 0

                pos += 4

            elif int(instructions[pos][-2:]) == 9:
                for i in range(1):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    elif param_list[i] == 1:
                        op_list[i] = pos+1+i
                    elif param_list[i] == 2:
                        op_list[i] = relative_base + int(instructions[pos+1+i])
                op_list = list(map(lambda x: int(x), op_list))

                relative_base += int(instructions[op_list[0]])
                pos += 2

            else:
                return

if __name__ == "__main__":
    main()
