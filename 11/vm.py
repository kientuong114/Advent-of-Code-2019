from collections import defaultdict
from intcode import *

with open("input.txt") as f:
    s = f.read().strip()

mem = [int(x) for x in s.split(",")]

def run_robot(mem, grid):
    robot = IntCodeCPU(mem[:])
    seen = set()
    x, y, d = 0, 0, 0
    ds = [(0,1),(1,0),(0,-1),(-1,0)]

    while True:
        robot.queue_input(grid[(x,y)])
        last = robot.run_until(Opcode.OUT)
        if last == Opcode.HALT:
            break
        color = robot.get_last_output()
        grid[(x,y)] = color
        seen.add((x,y))
        last = robot.run_until(Opcode.OUT)
        if last == Opcode.HALT:
            break
        turn = robot.get_last_output()
        if turn == 0:
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4
        x += ds[d][0]
        y += ds[d][1]
    return seen

robot.queue_input(1)
grid = defaultdict(lambda:0)
print(len(run_robot(mem, grid)))

grid = defaultdict(lambda:0)
grid[(0,0)] = 1
run_robot(mem, grid)
x_bounds = (min(p[0] for p in grid) - 1, max(p[0] for p in grid) + 2, 1)
y_bounds = (max(p[1] for p in grid) + 1, min(p[1] for p in grid) - 2, -1)
print("\n".join("".join(" #"[grid[(i,j)]] for i in range(*x_bounds)) \
                for j in range(*y_bounds)))

