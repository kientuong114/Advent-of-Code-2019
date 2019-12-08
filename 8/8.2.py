import sys

width = 25
height = 6

def main():
    inputString = open("input.txt").readline().strip('\n').replace('0', '3').replace('2','0')
    inputFile = [[inputString[i:i+width] for i in range(0, len(inputString), width)][j:j+height] for j in range(0, len(inputString)//width, height)]
    img = [list(map(lambda x: str(int(''.join(x)))[0], zip(*elem))) for elem in list(map(list, zip(*inputFile)))]

    for row in img:
        for elem in row:
            if elem == '1':
                sys.stdout.write('o')
            else:
                sys.stdout.write(' ')
        sys.stdout.write('\n')

    """
    inputFile = open("input.txt").readline().strip('\n').replace('0', '3').replace('2','0')
    inputFile = [inputFile[i:i+(width*height)] for i in range(0,len(inputFile), width*height)]
    inputFile = list(map(lambda x: [x[i:i+width] for i in range(0, len(x), width)], inputFile))
    compact = list(map(list, zip(*inputFile)))
    newCompact = []
    for elem in compact:
        newCompact.append(list(map(lambda x: int(''.join(x)), zip(*elem))))
    image = []
    for row in newCompact:
        newRow = []
        for elem in row:
            newRow.append(str(elem)[0])
        image.append(newRow)

    for row in image:
        print(row)
    """

if __name__ == "__main__":
    main()

