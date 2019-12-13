import sys
import math
import itertools
from functools import reduce
from math import gcd

def lcm(x, y, z):
    gcd2 = gcd(y, z)
    gcd3 = gcd(x, gcd2)

    lcm2 = y*z // gcd2
    lcm3 = x*lcm2 // gcd(x, lcm2)
    return lcm3

def main():
    moons = dict()
    XSet = set()
    YSet = set()
    ZSet = set()
    Xfound = False
    Yfound = False
    Zfound = False
    found_times = [0,0,0]
    inputFile = list(map(lambda x: x.strip('\n')[1:-1].replace(" ","").split(','), open("input.txt").readlines()))
    inputFile = list(map(lambda x: list(map(lambda y: int(y[2:]), x)), inputFile))
    for key, elem in enumerate(inputFile):
        moons.update({key: {"x": elem[0], "y": elem[1], "z":elem[2], "vx": 0, "vy": 0, "vz": 0}})

    i = 1
    while True:
        print(i)
        for couple in itertools.combinations(moons.items(), 2):
            if couple[0][1]['x'] > couple[1][1]['x']:
                couple[0][1]['vx'] -= 1
                couple[1][1]['vx'] += 1
            if couple[0][1]['x'] < couple[1][1]['x']:
                couple[0][1]['vx'] += 1
                couple[1][1]['vx'] -= 1
            if couple[0][1]['y'] > couple[1][1]['y']:
                couple[0][1]['vy'] -= 1
                couple[1][1]['vy'] += 1
            if couple[0][1]['y'] < couple[1][1]['y']:
                couple[0][1]['vy'] += 1
                couple[1][1]['vy'] -= 1
            if couple[0][1]['z'] > couple[1][1]['z']:
                couple[0][1]['vz'] -= 1
                couple[1][1]['vz'] += 1
            if couple[0][1]['z'] < couple[1][1]['z']:
                couple[0][1]['vz'] += 1
                couple[1][1]['vz'] -= 1
        toAddX = []
        toAddY = []
        toAddZ = []
        for elem in moons.items():
            elem[1]['x'] += elem[1]['vx']
            elem[1]['y'] += elem[1]['vy']
            elem[1]['z'] += elem[1]['vz']
            toAddX = toAddX + [elem[1]['x'], elem[1]['vx']]
            toAddY = toAddY + [elem[1]['y'], elem[1]['vy']]
            toAddZ = toAddZ + [elem[1]['z'], elem[1]['vz']]
        #print(toAddX, XSet, toAddY, YSet, toAddZ, ZSet)
        if tuple(toAddX) in XSet and not Xfound:
            print("found x")
            found_times[0] = i-1
            Xfound = True
        else:
            XSet.add(tuple(toAddX))
        if tuple(toAddY) in YSet and not Yfound:
            print("found y")
            found_times[1] = i-1
            Yfound = True
        else:
            YSet.add(tuple(toAddY))
        if tuple(toAddZ) in ZSet and not Zfound:
            print("found z")
            found_times[2] = i-1
            Zfound = True
        else:
            ZSet.add(tuple(toAddZ))
        if Xfound and Yfound and Zfound:
            break
        i+=1
    print(found_times)
    print(lcm(*found_times))
    

if __name__ == "__main__":
    main()
