import sys
import itertools

firstTime = [True]*5

def runMachine(mNum, inputSig, phase = -1, savedPos = 0, savedConf = None, lastOutputSig = -1):
    global firstTime
    with open("input.txt") as f:
        instructions = f.read().strip('\n').split(',')
        start_memory = list(map(lambda x: x, instructions))
        start = True
        pos = savedPos
        outputSig = -1
        if savedConf is None:
            instructions = list(start_memory)
        else:
            instructions = savedConf
        while instructions[pos][-2:] != "99":
            n_params = len(instructions[pos]) - 2
            param_list = [0,0,0]
            op_list = [0,0,0]

            for i in range(n_params):
                param_list[i] = instructions[pos][-3-i]

            param_list = list(map(lambda x: int(x), param_list))

            if int(instructions[pos][-2:]) == 1:
                for i in range(3):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    else:
                        op_list[i] = pos+1+i

                op_list = list(map(lambda x: int(x), op_list))
                
                instructions[op_list[2]] = str(int(instructions[op_list[0]]) + int(instructions[op_list[1]]))
                pos += 4
                    
            elif int(instructions[pos][-2:]) == 2:
                for i in range(3):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    else:
                        op_list[i] = pos+1+i
                op_list = list(map(lambda x: int(x), op_list))

                instructions[op_list[2]] = str(int(instructions[op_list[0]]) * int(instructions[op_list[1]]))
                pos += 4

            elif int(instructions[pos][-2:]) == 3:
                for i in range(1):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    else:
                        op_list[i] = pos+1+i
                op_list = list(map(lambda x: int(x), op_list))
                if firstTime[mNum]:
                    val = phase
                    firstTime[mNum] = False
                else:
                    val = inputSig
                instructions[op_list[0]] = str(val)
                pos += 2

            elif int(instructions[pos][-2:]) == 4:
                for i in range(1):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    else:
                        op_list[i] = pos+1+i
                op_list = list(map(lambda x: int(x), op_list))
                outputSig = instructions[op_list[0]]
                pos += 2
                return outputSig, pos, instructions, False

            elif int(instructions[pos][-2:]) == 5:
                for i in range(2):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    else:
                        op_list[i] = pos+1+i
                op_list = list(map(lambda x: int(x), op_list))
                if int(instructions[op_list[0]]) != 0:
                    pos = int(instructions[op_list[1]])
                else: 
                    pos += 3
            elif int(instructions[pos][-2:]) == 6:
                for i in range(2):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    else:
                        op_list[i] = pos+1+i
                op_list = list(map(lambda x: int(x), op_list))
                if int(instructions[op_list[0]]) == 0:
                    pos = int(instructions[op_list[1]])
                else: 
                    pos += 3
            elif int(instructions[pos][-2:]) == 7:
                for i in range(3):
                    if param_list[i] == 0:
                        op_list[i] = instructions[pos+1+i]
                    else:
                        op_list[i] = pos+1+i
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
                    else:
                        op_list[i] = pos+1+i
                op_list = list(map(lambda x: int(x), op_list))
                if int(instructions[op_list[0]]) == int(instructions[op_list[1]]):

                    instructions[op_list[2]] = 1
                else:
                    instructions[op_list[2]] = 0

                pos += 4
            else:
                return
        if outputSig == -1:
            outputSig = lastOutputSig
        return outputSig, pos, instructions, True

def main():
    global firstTime
    configSet = set()
    for i in itertools.permutations([5,6,7,8,9]):
        firstTime = [True for _ in range(5)]
        out0 = 0
        pos0 = 0
        config0 = 0
        out0, pos0, config0, fin = runMachine(0, 0, i[0])
        out1, pos1, config1, fin = runMachine(1, out0, i[1])
        out2, pos2, config2, fin = runMachine(2, out1, i[2])
        out3, pos3, config3, fin = runMachine(3, out2, i[3])
        out4, pos4, config4, fin = runMachine(4, out3, i[4])
        while not fin:
            out0, pos0, config0, fin = runMachine(0, out4, i[0], pos0, config0, out0)
            out1, pos1, config1, fin = runMachine(1, out0, i[1], pos1, config1, out1)
            out2, pos2, config2, fin = runMachine(2, out1, i[2], pos2, config2, out2)
            out3, pos3, config3, fin = runMachine(3, out2, i[3], pos3, config3, out3)
            out4, pos4, config4, fin = runMachine(4, out3, i[4], pos4, config4, out4)
        configSet.add(int(out4))

    print(max(configSet))
        


if __name__ == "__main__":
    main()
