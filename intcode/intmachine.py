import sys
import queue
import pprint
import math
import copy
from collections import deque
from functools import reduce

class intMachine:
    def __init__(self, memory: list, startPos = 0):
        if isinstance(memory, str):
            self.__memory = list(map(lambda x: int(x), open(memory).strip('\n').split(',')))
        else:
            self.__memory = memory
        self.__pos = startPos                   #Used to resume execution after pause
        self.__instructionSet = dict()          #Dict of all instructions, with the natural language name
        self.__inputQueue = deque()       #Queue for inputs
        self.__opCodeMapper = dict()            #Dict of all instructions, indexed by opcode

    def __init__(self, prototype):
        self.__memory = prototype.getMemory()
        self.__pos = prototype.getPos()
        self.__inputQueue = copy.deepcopy(prototype.getQueue())
        self.__opCodeMapper = copy.deepcopy(prototype.getOpCodeMapper())

    def addArithmeticInstruction(self, name, opcode, func, nOperands, hasOutput):
        self.__instructionSet.update({name: {"function": func, "nOperands": nOperands, "type": "arithmetic", "hasOutput": hasOutput}})
        self.__opCodeMapper.update({opcode: name})

    def __execArithmeticInstruction(self, instruction, *operands):
        return reduce(instruction, operands)
    
    def addLogicInstruction(self, name, opcode, func, nOperands, hasOutput):
        self.__instructionSet.update({name: {"function": func, "nOperands": nOperands, "type": "logic", "hasOutput": hasOutput}})
        self.__opCodeMapper.update({opcode: name})

    def __execLogicInstruction(self, instruction, *operands):
        return instruction(*operands)

    def addBranchInstruction(self, name, opcode, func, nOperands, hasOutput):
        #nOperands includes the destination operand
        self.__instructionSet.update({name: {"function": func, "nOperands": nOperands, "type": "branch", "hasOutput": hasOutput}})
        self.__opCodeMapper.update({opcode: name})

    def __execBranchInstruction(self, instruction, destination, *operands):
        if instruction(*operands):
            self.__pos = destination
        else:
            self.__pos += len(operands) + 2
        return
    
    def addReadInstruction(self, opcode):
        self.__instructionSet.update({"read": {"function": None, "nOperands": 1, "type": "io", "hasOutput": True}})
        self.__opCodeMapper.update({opcode: "read"})

    def execInstruction(self, name, *operands):
        instruction = self.__instructionSet[name]['function']
        nOperands = self.__instructionSet[name]['nOperands']
        instructionType = self.__instructionSet[name]['type']
        hasOutput = self.__instructionSet[name]['hasOutput']

        if len(operands) > nOperands:
            raise Exception("Too many operands given")

        if instructionType  == "arithmetic":
            self.__pos += 1 + nOperands + (1 if hasOutput else 0)
            return self.__execArithmeticInstruction(instruction, *operands)
        elif instructionType == "logic":
            self.__pos += 1 + nOperands + (1 if hasOutput else 0)
            return self.__execLogicInstruction(instruction, *operands)
        elif instructionType == "branch":
            return self.__execBranchInstruction(instruction, operands[-1], *operands[:-1])

    def opCodeTranslate(self, opcode):
        if opcode in self.__opCodeMapper:
            return self.__opCodeMapper[opcode]
        else:
            raise Exception("No such opcode found")

    def fullExecutionStart(self, startPos = 0):
        #Execution that tries to get from start to end, if the program tries to fetch an input from an empty queue, the program crashes
        pos = startPos
        while readMem(pos) != 99:
            instructionName = opCodeTranslate(readMem(pos))


    def addInput(self, val):
        self.inputQueue.put(val)

    def getPos(self):
        return self.__pos

    def setPos(self, val):
        self.__pos = val

    def getInput(self):
        if q.empty():
            raise Exception("Trying to extract values from empty input queue")
        return self.__inputQueue.get()

    def readMem(self, pos):
        return self.__memory[pos]

    def getMemory(self):
        return list(self.__memory)

    def getQueue(self):
        return self.__inputQueue

    def getOpCodeMapper(self):
        return self.__opCodeMapper

    def printMemory(self, lineSize = 10, cellSize = 8):
        print("Printing memory")
        print("---------------")
        memMatrix = [self.__memory[i:i+lineSize] for i in range(0, len(self.__memory), lineSize)]
        memMatrix[-1] = memMatrix[-1] + (lineSize-len(memMatrix[-1])) * ['---']
        line = 0
        for elem in memMatrix:
            sys.stdout.write("["+str(line).rjust(4)+"]")
            for cell in elem:
                sys.stdout.write(str(cell).rjust(cellSize))
            sys.stdout.write("|\n")
            line += lineSize

    def printInstructionSet(self):
        pp = pprint.PrettyPrinter(indent = 4)
        pp.pprint(self.__instructionSet)

def main():
    m1 = intMachine([1,2,3,4,5,6,7,8,9,10,11,12,2,23,4,5,6,23, 24, 25, 26])
    m1.printMemory()

if __name__ == "__main__":
    main()
