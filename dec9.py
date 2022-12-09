"""
A rope is represented by H and T, the head and tail, and because the rope is quite short, the head and tail must always be touching 
(diagonally, horizontally, vertically, or even overlapping.)

If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:
.....    .....    .....
.TH.. -> .T.H. -> ..TH.
.....    .....    .....

Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:
.....    .....    .....
.....    ..H..    ..H..
..H.. -> ..... -> ..T..
.T...    .T...    .....
.....    .....    .....

Given a series of movements as the input, work out where the tail goes as it follows the head.
Assume they both start together at the same position, overlapping, and can move freely an unlimited distance in any direction.
"""
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "dec9_input.txt"))
lines = f.read().splitlines()

part = 2

# Part 1
# Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?
if part == 1:
    # method:
    # keep track of all positions relative to the start position: (0,0)
    # use a set of tuples to keep track of what positions have been moved over by the tail.
    # update the head and the tail positions with each movement. line[0] is direction, line [2:] is number of units
    # after all the movements have been executed, return the size of the set.

    head = (0,0)
    tail = (0,0)
    visited = set()
    visited.add(tail)

    for line in lines:
        direction = line[0]
        distance = int(line[2:])
        horizontal = True

        for i in range(0, distance):
            if direction == "R":
                head = (head[0] + 1, head[1])
            elif direction == "L":
                head = (head[0] - 1, head[1])
            elif direction == "U":
                head = (head[0], head[1] + 1)
                horizontal = False
            elif direction == "D":
                head = (head[0], head[1] - 1)
                horizontal = False

            if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:

                if horizontal and head[1] != tail[1]:           
                    tail = (tail[0], head[1])
                elif not horizontal and head[0] != tail[0]:
                    tail = (head[0], tail[1])

                if horizontal:
                    if direction == "R":
                        tail = (tail[0] + 1, tail[1])
                    else:
                        tail = (tail[0] - 1, tail[1])
                else:
                    if direction == "U":
                        tail = (tail[0], tail[1] + 1)
                    else:
                        tail = (tail[0], tail[1] - 1)
                visited.add(tail)
    print(len(visited))
    # ans: 6339

# Part 2
# The rope now has ten knots that cover ten spaces. The head is the front, the tail is the back.
# each knot follows the knot in front of it in the same way as part 1.
# we still only need to keep track of what positions the last knot covers.
elif part == 2:
    # new method:
    # instead of moving head and then tail like before,
    # move head, then next knot, then next knot, etc... 1 unit at a time. 
    
    rope = [(0,0) for i in range(10)]
    
    visited = set()
    visited.add((0,0))

    DIRECTIONS = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1)
    }

    rope = [(0,0) for i in range(10)]
    
    for line in lines:
        direction = DIRECTIONS[line[0]]
        distance = int(line[2:])

        for i in range(distance):
            a = rope[0]
            rope[0] = a[0] + direction[0], a[1] + direction[1]
            for j in range(1, 10):
                # rope[x] = follow(rope[x-1], rope[x])
                head = rope[j-1]
                tail = rope[j]

                x, y = head[0] - tail[0], head[1] - tail[1]
                abs_x = abs(x)
                abs_y = abs(y)
                
                if abs_x > 1 or abs_y > 1:                   
                    tail = (tail[0] + (0 if x == 0 else x // abs_x), tail[1] + (0 if y == 0 else y // abs_y))
                rope[j] = tail

            visited.add(rope[-1])
    
    print(len(visited))
    # ans: 2541

f.close()