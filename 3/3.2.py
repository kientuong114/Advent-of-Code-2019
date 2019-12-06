import sys

pSet = set()
dDict = dict()
interDict = dict()

def main():
    inputFile = list(map(lambda x: x.split(','), open("input.txt").readlines()))
    x = 0
    y = 0
    d1 = 0
    for elem in inputFile[0]:
        if elem[0] == 'L':
            for _ in range(0, int(elem[1:])):
                x -= 1
                d1 += 1
                pSet.add((x,y))
                dDict.update({(x,y):d1})
        if elem[0] == 'U':
            for _ in range(0, int(elem[1:])):
                y += 1
                d1 += 1
                pSet.add((x,y))
                dDict.update({(x,y):d1})
        if elem[0] == 'R':
            for _ in range(0, int(elem[1:])):
                x += 1 
                d1 += 1
                pSet.add((x,y))
                dDict.update({(x,y):d1})
        if elem[0] == 'D':
            for _ in range(0, int(elem[1:])):
                y -= 1
                d1 += 1
                pSet.add((x,y))
                dDict.update({(x,y):d1})

    x = 0
    y= 0
    d1 = 0
                
    for elem in inputFile[1]:
        if elem[0] == 'L':
            for _ in range(0, int(elem[1:])):
                x -= 1
                d1 += 1
                if (x,y) in pSet:
                    interDict.update({(x,y): dDict[(x,y)] + d1})
        if elem[0] == 'U':
            for _ in range(0, int(elem[1:])):
                y += 1
                d1 += 1
                if (x,y) in pSet:
                    interDict.update({(x,y): dDict[(x,y)] + d1})
        if elem[0] == 'R':
            for _ in range(0, int(elem[1:])):
                x += 1 
                d1 += 1
                if (x,y) in pSet:
                    interDict.update({(x,y): dDict[(x,y)] + d1})
        if elem[0] == 'D':
            for _ in range(0, int(elem[1:])):
                y -= 1
                d1 += 1
                if (x,y) in pSet:
                    interDict.update({(x,y): dDict[(x,y)] + d1})

    maxDist = sys.maxsize

    for (x,y), value in interDict.items():
        if value < maxDist:
            maxDist = value
    
    print(maxDist)
    

if __name__ == "__main__":
    main()
