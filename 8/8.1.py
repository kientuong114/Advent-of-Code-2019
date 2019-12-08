import sys
import math
import itertools
from functools import reduce
from collections import Counter



def main():
    inputFile = open("input.txt").readline().strip('\n')
    inputFile = [inputFile[i:i+(25*6)] for i in range(0,len(inputFile), 25*6)]
    inputFile = list(map(lambda x: [x[i:i+25] for i in range(0, len(x), 25)], inputFile))
    print(inputFile)
    minOccur = [1000000000000,0,0]
    for layer in inputFile:
        nChar = [0,0,0]
        for row in layer:
            nChar[0] += Counter(row)['0']
            nChar[1] += Counter(row)['1']
            nChar[2] += Counter(row)['2']

        print(nChar)
        if nChar[0] < minOccur[0]:
            minOccur = list(nChar)
    print(minOccur[1]*minOccur[2])
            







if __name__ == "__main__":
    main()

