"""



"""


import os
from collections import deque

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "dec10_input.txt"))
lines = f.read().splitlines()

part = 1

# Part 1
if part == 1:
    x = 1
    signal = 0
    cycle = 0
    nextSignalAt = 20
    for line in lines:
        instruction = line[:4]

        if cycle + 2 >= nextSignalAt:
            signal += (x * nextSignalAt)
            nextSignalAt += 40

        if instruction == "noop":
            cycle += 1
        else:
            cycle += 2
            val = int(line[5:].strip())
            x += val

        # print("it is the start of cycle " + str(cycle) + " and x = " + str(x))
    print("signal = " + str(signal))
    # ans: 11780

# Part 2
elif part == 2:
    # ...wha?
    pass

f.close()