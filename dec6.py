"""
The puzzle input is a single line this time.
What we have to find is the 4-character group in the input that have no repeating characters.
"""


part = 2

from collections import deque
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "dec6_input.txt"))
line = f.read()

# sample_input = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

"""
dq = deque()
dq.append("x")
dq.append("y")
dq.append("z")
print(dq)
dq.popleft()
print(dq)
"""

# Part 1
# How many characters need to be processed before the first start-of-packet marker is detected?
if part == 1:

    # method:
    # -maintain a queue of 4 characters, popping the oldest and adding the newest characters
    # -if ever all the characters in the queue are different and the length of the queue is 4, 
    #  then return the number of characters read so far.
    characters_read = 0
    dq = deque()
    for letter in line:
        characters_read += 1
        if len(dq) < 4:
            dq.appendleft(letter)
        else:
            dq.pop()
            dq.appendleft(letter)
            if not any(dq.count(x) > 1 for x in dq):
                break

        # print("characters_read = " + str(characters_read) + " | dq = " + str(dq))
    # print("END; characters_read = " + str(characters_read) + " | dq = " + str(dq))
    print("characters_read = " + str(characters_read))
    # ans: 1929


# Part 2
# What's changed? We're doing the same thing but with a group of 14 characters now.
# How many characters need to be processed before the first start-of-message marker is detected?
elif part == 2:
    characters_read = 0
    dq = deque()
    for letter in line:
        characters_read += 1
        if len(dq) < 14:
            dq.appendleft(letter)
        else:
            dq.pop()
            dq.appendleft(letter)
            if not any(dq.count(x) > 1 for x in dq):
                break

    print("characters_read = " + str(characters_read))
    # ans: 3298

f.close()