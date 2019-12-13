import sys
import math
import itertools
from functools import reduce


def main():
    moons = dict()
    inputFile = list(map(lambda x: x.strip('\n')[1:-1].replace(" ","").split(','), open("input.txt").readlines()))
    inputFile = list(map(lambda x: list(map(lambda y: int(y[2:]), x)), inputFile))
    for key, elem in enumerate(inputFile):
        moons.update({key: {"x": elem[0], "y": elem[1], "z":elem[2], "vx": 0, "vy": 0, "vz": 0}})

    for i in range(1000):
        print("STEP ", i)
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
        for elem in moons.items():
            elem[1]['x'] += elem[1]['vx']
            elem[1]['y'] += elem[1]['vy']
            elem[1]['z'] += elem[1]['vz']
    energy = 0
    for moon in moons.items():
        kinenergy = 0
        potenergy = 0
        kinenergy += abs(moon[1]['x'])+abs(moon[1]['y'])+abs(moon[1]['z'])
        potenergy += abs(moon[1]['vx'])+abs(moon[1]['vy'])+abs(moon[1]['vz'])
        energy += kinenergy * potenergy
    print(energy)





if __name__ == "__main__":
    main()
