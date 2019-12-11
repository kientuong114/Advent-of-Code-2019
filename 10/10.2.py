import math

def canSeeTarget(source, dest, astSet):
    dx = dest[0]-source[0]
    dy = dest[1]-source[1]
    d = math.gcd(dx, dy)
    dx = dx//d
    dy = dy//d
    xp = source[0] + dx
    yp = source[1] + dy
    while True:
        if(xp, yp) == dest:
            return True
        if (xp, yp) in astSet:
            return False
        xp += dx
        yp += dy

def main():

    inputFile = list(map(lambda x: list(x.strip('\n')), open("input.txt").readlines()))
    width = len(inputFile)
    height = len(inputFile[0])
    astSet = set()
    for row_n, row in enumerate(inputFile):
        for col_n, col in enumerate(row):
            if col == '#':
                astSet.add((row_n, col_n))

    maxSeen = 0
    for source in astSet:
        noSee = set()
        noSee.add(source)
        for dest in astSet:
            if source == dest:
                continue
            dx = dest[0]-source[0]
            dy = dest[1]-source[1]
            d = math.gcd(dx, dy)
            dx = dx//d
            dy = dy//d
            xp = source[0] + dx
            yp = source[1] + dy
            while True:
                if(xp, yp) == dest:
                    break
                if (xp, yp) in astSet:
                    noSee.add(dest)
                    break
                xp += dx
                yp += dy
                
        canSee = astSet.difference(noSee)
        if len(canSee) > maxSeen:
            maxSeen = len(canSee)
            maxAst1 = source

    maxAst = (maxAst1[1], maxAst1[0])

    hitCount = 0


    targetNum = 200

    while True:
        upHittable = maxAst
        downHittable = maxAst
        leftHittable = set()
        rightHittable = set()
        removed = []
        astSet = set(map(lambda x: (x[1], x[0]), astSet))

        for i in range(maxAst[1]-1, -1, -1):
            if (maxAst[0], i) in astSet:
                upHittable = (maxAst[0], i)
                break
        for i in range(maxAst[1]+1, height):
            if (maxAst[0], i) in astSet:
                downHittable = (maxAst[0], i)
                break
        for p in astSet:
            if p != maxAst and p != upHittable and p != downHittable and canSeeTarget(maxAst, p, astSet):
                if p[0] > maxAst[0]:
                    rightHittable.add(p)
                else:
                    leftHittable.add(p)

        if upHittable != maxAst:
            hitCount += 1
            removed.append((hitCount, upHittable))
            if hitCount == targetNum:
                break

        targeted = list(map(lambda x: (x, math.atan((x[1]-maxAst[1])/(x[0]-maxAst[0]))), rightHittable))
        targeted.sort(key=lambda x: x[1])
        for elem in targeted:
            hitCount += 1
            removed.append((hitCount, elem[0]))
            if hitCount == targetNum:
                break

        if downHittable != maxAst:
            hitCount += 1
            removed.append((hitCount, downHittable))
            if hitCount == targetNum:
                break
            
        targeted = list(map(lambda x: (x, math.atan((x[1]-maxAst[1])/(x[0]-maxAst[0]))), leftHittable))
        targeted.sort(key=lambda x: x[1])
        for elem in targeted:
            hitCount += 1
            removed.append((hitCount, elem[0]))
            if hitCount == targetNum:
                break

        if hitCount == targetNum:
            for k, p in removed:
                print("[",k,"] ",p)
            return

        for elem in removed:
            astSet.remove(elem)



if __name__ == "__main__":
    main()
