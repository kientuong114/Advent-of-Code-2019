import itertools
import sys

def binarySearch(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return mid
    return -1

def main():
    vertexSet = set()
    inputFile = list(map(lambda x: x.strip("\n").split(")"), open("input.txt").readlines()))
    for elem in inputFile:
        vertexSet.add(elem[0])
        vertexSet.add(elem[1])

    vertexList = sorted(vertexSet)

    matrix = [[0]*len(vertexSet) for _ in range(len(vertexSet))]
    matrix2 = [[0]*len(vertexSet) for _ in range(len(vertexSet))]

    for elem in inputFile:
        i1 = binarySearch(vertexList, elem[0])
        i2 = binarySearch(vertexList, elem[1])
        matrix[i2][i1] = 1
        matrix[i1][i2] = 1

    you = binarySearch(vertexList, "YOU")
    vertexStack = [("YOU", you, 0)]
    doneVertices = set()

    while len(vertexStack):
        toSearch = vertexStack.pop(0)
        doneVertices.add(toSearch[1])
        if toSearch[0] == "SAN":
            print(toSearch[2]-2)
            return
        for i in range(len(matrix)):
            if matrix[toSearch[1]][i] == 1 and i not in doneVertices:
                vertexStack.append((vertexList[i], i, toSearch[2]+1))

if __name__ == "__main__":
    main()
