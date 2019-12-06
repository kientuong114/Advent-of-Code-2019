import math

with open("input.txt") as f:
    inputArr = f.readlines()
    inputArr = map(lambda x: float(x), inputArr)
    accum = 0
    for elem in inputArr:
        result = elem
        first = True
        while result > 0:
            if not first:
                accum += result
            else:
                first = False
            result = math.floor(result/3)-2

print(accum)


