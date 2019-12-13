import sys

inputQueue = []
outputQueue = []


class Machine:
    def __init__(self):
        with open("input.txt") as f:
            self.instructions = f.read().strip('\n').split(',')
            start_memory = list(map(lambda x: x, self.instructions))
            self.pos = 0
            self.instructions = list(start_memory) + ['0' for _ in range(1000)]
            self.relative_base = 0

    def machineStart(self):
        global inputQueue
        global outputQueue
        while self.instructions[self.pos][-2:] != "99":
            print(self.pos, self.instructions[self.pos], self.instructions[self.pos+1], self.instructions[self.pos+1])
            n_params = len(self.instructions[self.pos]) - 2
            param_list = [0,0,0]
            op_list = [0,0,0]

            for i in range(n_params):
                param_list[i] = self.instructions[self.pos][-3-i]

            param_list = list(map(lambda x: int(x), param_list))

            if int(self.instructions[self.pos][-2:]) == 1:
                for i in range(3):
                    if param_list[i] == 0:
                        op_list[i] = self.instructions[self.pos+1+i]
                    elif param_list[i] == 1:
                        op_list[i] = self.pos+1+i
                    elif param_list[i] == 2:
                        op_list[i] = self.relative_base + int(self.instructions[self.pos+1+i])

                op_list = list(map(lambda x: int(x), op_list))
                
                self.instructions[op_list[2]] = str(int(self.instructions[op_list[0]]) + int(self.instructions[op_list[1]]))
                self.pos += 4
                    
            elif int(self.instructions[self.pos][-2:]) == 2:
                for i in range(3):
                    if param_list[i] == 0:
                        op_list[i] = self.instructions[self.pos+1+i]
                    elif param_list[i] == 1:
                        op_list[i] = self.pos+1+i
                    elif param_list[i] == 2:
                        op_list[i] = self.relative_base + int(self.instructions[self.pos+1+i])
                op_list = list(map(lambda x: int(x), op_list))

                self.instructions[op_list[2]] = str(int(self.instructions[op_list[0]]) * int(self.instructions[op_list[1]]))
                self.pos += 4

            elif int(self.instructions[self.pos][-2:]) == 3:
                for i in range(1):
                    if param_list[i] == 0:
                        op_list[i] = self.instructions[self.pos+1+i]
                    elif param_list[i] == 1:
                        op_list[i] = self.pos+1+i
                    elif param_list[i] == 2:
                        op_list[i] = self.relative_base + int(self.instructions[self.pos+1+i])
                op_list = list(map(lambda x: int(x), op_list))
                if len(inputQueue) == 0:
                    return
                else:
                    val = inputQueue.pop(0)
                self.instructions[op_list[0]] = str(val)
                self.pos += 2

            elif int(self.instructions[self.pos][-2:]) == 4:
                for i in range(1):
                    if param_list[i] == 0:
                        op_list[i] = self.instructions[self.pos+1+i]
                    elif param_list[i] == 1:
                        op_list[i] = self.pos+1+i
                    elif param_list[i] == 2:
                        op_list[i] = self.relative_base + int(self.instructions[self.pos+1+i])
                op_list = list(map(lambda x: int(x), op_list))
                outputQueue.append(int(self.instructions[op_list[0]]))
                print("output: "+str(self.instructions[op_list[0]]))
                self.pos += 2

            elif int(self.instructions[self.pos][-2:]) == 5:
                for i in range(2):
                    if param_list[i] == 0:
                        op_list[i] = self.instructions[self.pos+1+i]
                    elif param_list[i] == 1:
                        op_list[i] = self.pos+1+i
                    elif param_list[i] == 2:
                        op_list[i] = self.relative_base + int(self.instructions[self.pos+1+i])
                op_list = list(map(lambda x: int(x), op_list))
                if int(self.instructions[op_list[0]]) != 0:
                    self.pos = int(self.instructions[op_list[1]])
                else: 
                    self.pos += 3
            elif int(self.instructions[self.pos][-2:]) == 6:
                for i in range(2):
                    if param_list[i] == 0:
                        op_list[i] = self.instructions[self.pos+1+i]
                    elif param_list[i] == 1:
                        op_list[i] = self.pos+1+i
                    elif param_list[i] == 2:
                        op_list[i] = self.relative_base + int(self.instructions[self.pos+1+i])
                op_list = list(map(lambda x: int(x), op_list))
                if int(self.instructions[op_list[0]]) == 0:
                    self.pos = int(self.instructions[op_list[1]])
                else: 
                    self.pos += 3
            elif int(self.instructions[self.pos][-2:]) == 7:
                for i in range(3):
                    if param_list[i] == 0:
                        op_list[i] = self.instructions[self.pos+1+i]
                    elif param_list[i] == 1:
                        op_list[i] = self.pos+1+i
                    elif param_list[i] == 2:
                        op_list[i] = self.relative_base + int(self.instructions[self.pos+1+i])
                op_list = list(map(lambda x: int(x), op_list))
                if int(self.instructions[op_list[0]]) < int(self.instructions[op_list[1]]):
                    self.instructions[op_list[2]] = 1
                else:
                    self.instructions[op_list[2]] = 0

                self.pos += 4

            elif int(self.instructions[self.pos][-2:]) == 8:
                for i in range(3):
                    if param_list[i] == 0:
                        op_list[i] = self.instructions[self.pos+1+i]
                    elif param_list[i] == 1:
                        op_list[i] = self.pos+1+i
                    elif param_list[i] == 2:
                        op_list[i] = self.relative_base + int(self.instructions[self.pos+1+i])
                op_list = list(map(lambda x: int(x), op_list))

                if int(self.instructions[op_list[0]]) == int(self.instructions[op_list[1]]):

                    self.instructions[op_list[2]] = 1
                else:
                    self.instructions[op_list[2]] = 0

                self.pos += 4

            elif int(self.instructions[self.pos][-2:]) == 9:
                for i in range(1):
                    if param_list[i] == 0:
                        op_list[i] = self.instructions[self.pos+1+i]
                    elif param_list[i] == 1:
                        op_list[i] = self.pos+1+i
                    elif param_list[i] == 2:
                        op_list[i] = self.relative_base + int(self.instructions[self.pos+1+i])
                op_list = list(map(lambda x: int(x), op_list))

                self.relative_base += int(self.instructions[op_list[0]])
                self.pos += 2
            elif int(self.instructions[self.pos][-2:]) == 99:
                outputQueue.append(99)
                print("terminated")
                return
            else:
                print("other stuff")
                return

def main():
    global inputQueue
    global outputQueue
    dirList = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    m1 = Machine()
    posPainted = dict()
    posWhitePainted = set()
    p = (0,0)
    direction = 0
    inputQueue.append(1)
    while(True):
        m1.machineStart()
        if len(outputQueue) == 0:
            break
        color = outputQueue.pop(0)
        if color == 99:
            break
        else:
            posPainted.update({p: color})
            if color == 1:
                posWhitePainted.add(p)
            turn = outputQueue.pop(0)
            if turn == 1:
                direction += 1
                direction %= 4
            else:
                direction -= 1
                direction %= 4
        p = (p[0] + dirList[direction][0], p[1]+dirList[direction][1])
        print(p)
        print(len(posPainted))
        if p in posPainted:
            print(posPainted[p])
        if (p not in posPainted) or (posPainted[p] == 0):
            inputQueue.append(0)
        elif posPainted[p] == 1:
            inputQueue.append(1)
        else:
            break
    minX = 0
    minY = 0
    maxX = 0
    maxY = 0
    for elem, stuff in posPainted.items():
        if elem[0] < minX:
            minX = elem[0]
        if elem[0] > maxX:
            maxX = elem[0]
        if elem[1] < minY:
            minY = elem[0]
        if elem[1] > maxY:
            maxY = elem[0]

    matrix = [[' ' for _ in range(180)] for a in range(maxY+minY+100)]

    for elem in posWhitePainted:
        matrix[elem[0]-minX][elem[1]-minY] = '@'

    for row in matrix:
        for elem in row:
            sys.stdout.write(elem)
        sys.stdout.write('\n')

    


        

    



if __name__ == "__main__":
    main()


