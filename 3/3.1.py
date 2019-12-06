import sys

pSet = set()
interSet = set()

def main():
    inputFile = list(map(lambda x: x.split(','), open("input.txt").readlines()))
    x = 0
    y = 0
    for elem in inputFile[0]:
        if elem[0] == 'L':
            for _ in range(0, int(elem[1:])):
                x -= 1
                pSet.add((x,y))
        if elem[0] == 'U':
            for _ in range(0, int(elem[1:])):
                y += 1
                pSet.add((x,y))
        if elem[0] == 'R':
            for _ in range(0, int(elem[1:])):
                x += 1 
                pSet.add((x,y))
        if elem[0] == 'D':
            for _ in range(0, int(elem[1:])):
                y -= 1
                pSet.add((x,y))

    x = 0
    y= 0
                
    for elem in inputFile[1]:
        if elem[0] == 'L':
            for _ in range(0, int(elem[1:])):
                x -= 1
                if (x,y) in pSet:
                    interSet.add((x,y))
        if elem[0] == 'U':
            for _ in range(0, int(elem[1:])):
                y += 1
                if (x,y) in pSet:
                    interSet.add((x,y))
        if elem[0] == 'R':
            for _ in range(0, int(elem[1:])):
                x += 1 
                if (x,y) in pSet:
                    interSet.add((x,y))
        if elem[0] == 'D':
            for _ in range(0, int(elem[1:])):
                y -= 1
                if (x,y) in pSet:
                    interSet.add((x,y))

    print(interSet)

    maxDist = sys.maxsize
    for elem in interSet:
        if abs(elem[0])+abs(elem[1]) < maxDist:
            maxDist = abs(elem[0])+abs(elem[1])
    
    print(maxDist)
    

if __name__ == "__main__":
    main()
