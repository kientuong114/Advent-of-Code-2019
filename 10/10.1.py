import math

def main():

    inputFile = list(map(lambda x: list(x.strip('\n')), open("input.txt").readlines()))
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

    print(maxSeen)

if __name__ == "__main__":
    main()
