import sys

def main():
    with open("input.txt") as f:
        instructions = f.read().strip('\n').split(',')
        start_memory = list(map(lambda x: x, instructions))
        start = True
        pos = 0
        instructions = list(start_memory)
        while instructions[pos][-2:] != "99":
            n_params = len(instructions[pos]) - 2
            param_list = [0,0,0]
            op_list = [0,0,0]
            print("pos: "+str(pos))

            for i in range(n_params):
                param_list[i] = instructions[pos][-3-i]

            param_list = list(map(lambda x: int(x), param_list))

            print(param_list)
            for index,elem in enumerate(instructions):
                sys.stdout.write("["+str(index)+"] "+str(elem)+", ")


            if int(instructions[pos][-2:]) == 1:
                for i in range(3):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    else:
                        op_list[i] = pos+1+i

                op_list = list(map(lambda x: int(x), op_list))
                
                instructions[op_list[2]] = str(int(instructions[op_list[0]]) + int(instructions[op_list[1]]))
                print("Adding "+ str(op_list[0]) + " + " + str(op_list[1]) + " to " + str(op_list[2]))
                pos += 4
                    
            elif int(instructions[pos][-2:]) == 2:
                for i in range(3):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    else:
                        op_list[i] = pos+1+i
                op_list = list(map(lambda x: int(x), op_list))

                instructions[op_list[2]] = str(int(instructions[op_list[0]]) * int(instructions[op_list[1]]))
                print("Mult "+ str(op_list[0]) + " + " + str(op_list[1]) + " to " + str(op_list[2]))
                pos += 4

            elif int(instructions[pos][-2:]) == 3:
                for i in range(1):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    else:
                        op_list[i] = pos+1+i
                op_list = list(map(lambda x: int(x), op_list))
                val = 1
                instructions[op_list[0]] = str(val)
                print("Saving 1 in "+str(op_list[0]))
                pos += 2

            elif int(instructions[pos][-2:]) == 4:
                for i in range(1):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    else:
                        op_list[i] = pos+1+i
                op_list = list(map(lambda x: int(x), op_list))
                print("["+str(pos)+"] output: "+instructions[op_list[0]])
                pos += 2

if __name__ == "__main__":
    main()
