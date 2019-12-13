import sys
import queue
import pprint
import math
import copy
from collections import deque
from functools import reduce

OPCODE_LENGTH = 2

class intMachine:
    def __init__(self, memory: list, startPos = 0):
        if isinstance(memory, str):
            self.__memory = list(map(lambda x: int(x), open(memory).strip('\n').split(',')))
        else:
            self.__memory = memory
        self.__pos = startPos                   #Used to resume execution after pause
        self.__instructionSet = dict()          #Dict of all instructions, indexed by opcode
        self.__inputQueue = deque()       #Queue for inputs
        self.__nameMapper = dict()            #Mapper from name to opcode, to allow to call instructions in natural language

    """
    def __init__(self, prototype: intMachine):
        self.__memory = prototype.getMemory()
        self.__pos = prototype.getPos()
        self.__inputQueue = copy.deepcopy(prototype.getQueue())
        self.__nameMapper = copy.deepcopy(prototype.getNameMapper())
    """

    def readMem(self, pos):
        return self.__memory[pos]

    def addArithmeticInstruction(self, name, opcode, func, nOperands, hasOutput):
        self.__instructionSet.update({opcode: {"function": func, "nOperands": nOperands, "type": "arithmetic", "hasOutput": hasOutput}})
        self.__nameMapper.update({name: opcode})

    def __execArithmeticInstruction(self, instruction, *operands):
        return reduce(instruction, operands)
    
    def addLogicInstruction(self, name, opcode, func, nOperands, hasOutput):
        self.__instructionSet.update({opcode: {"function": func, "nOperands": nOperands, "type": "logic", "hasOutput": hasOutput}})
        self.__nameMapper.update({name: opcode})

    def __execLogicInstruction(self, instruction, *operands):
        return instruction(*operands)

    def addBranchInstruction(self, name, opcode, func, nOperands, hasOutput):
        #nOperands includes the destination operand
        self.__instructionSet.update({opcode: {"function": func, "nOperands": nOperands, "type": "branch", "hasOutput": hasOutput}})
        self.__nameMapper.update({opcode: name})

    def __execBranchInstruction(self, instruction, destination, *operands):
        if instruction(*operands):
            self.__pos = destination
        else:
            self.__pos += len(operands) + 2
        return
    
    def getNumOperands(self, opcode):
        return self.__instructionSet[opcode]['nOperands']
    
    def addReadInstruction(self, opcode):
        self.__instructionSet.update({"read": {"function": None, "nOperands": 1, "type": "io", "hasOutput": True}})
        self.__nameMapper.update({"read": opcode})

    def execInstruction(self, opcode, *operands):
        instruction = self.__instructionSet[opcode]['function']
        nOperands = self.__instructionSet[opcode]['nOperands']
        instructionType = self.__instructionSet[opcode]['type']
        hasOutput = self.__instructionSet[opcode]['hasOutput']

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

    def translateName(self, name):
        if name in self.__nameMapper:
            return self.__nameMapper[name]
        else:
            raise Exception("No such instruction")

    def fullExecutionStart(self, startPos = 0):
        #Execution that tries to get from start to end, if the program tries to fetch an input from an empty queue, the program crashes
        pos = startPos
        while self.readMem(pos) != 99:
            instructionName = opCodeTranslate(self.readMem(pos))

    def asyncExecutionStart(self, startPos = 0):
        pos = startPos
        while self.readMem(pos) != 99:
            nOperands = self.getNumOperands(self.readMem(pos))
            modeList = list(map(lambda x: int(x), list(str(self.readMem(pos)[:OPCODE_LENGTH].zfill(nOperands)))))
            print(modeList)
            #operands = getOperands(nOperands, modeList)
            #execInstruction(readMem(pos))
            


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

    def getOperands(self, nOperands, operandsMode):
        return



    def getMemory(self):
        return list(self.__memory)

    def getQueue(self):
        return self.__inputQueue

    def getNameMapper(self):
        return self.__nameMapper

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
    m1 = intMachine([1,2,3])
    m1.addArithmeticInstruction("test", 1, lambda x, y: x+y, 2, True)
    m1.asyncExecutionStart()

if __name__ == "__main__":
    main()
