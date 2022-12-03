
"""
The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up with the following list:
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

input file: dec1_input.txt
return: integer
"""

part = 2

import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "dec1_input.txt"))
lines = f.read().splitlines()

# PART 1
# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
if part == 1:
    # method:
    # read the input file and put each line into an element of a list.
    # then, we can interpret it as follows:
    # -if a number, add to current elf calory count
    # -if a newline, then move on to a new elf.
    # keep a running max and return that.
    runningMax = 0
    localMax = 0
    for entry in lines:
        if entry == "":
            # reset
            runningMax = max(runningMax, localMax)
            localMax = 0
        else:
            # add
            localMax += int(entry)
            
    print(runningMax)
    f.close()
    # ans: 69626

# PART 2
# By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.
# To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.
# In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.
# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
elif part == 2:
    # method:
    # same as part 1, but now keep a running max list of the top three encountered.
    # in the end, return the sum of the top three. 
    runningMax = [0, 0, 0]
    localMax = 0
    for entry in lines:
        if entry == "":
            # reset

            # replace the minimum value of runningMax with localMax, if localMax is greater than it
            # otherwise, nothing
            if localMax > min(runningMax):
                runningMax[runningMax.index(min(runningMax))] = localMax
            localMax = 0
        else:
            # add
            localMax += int(entry)
            
    print(sum(runningMax))
    f.close()
    # ans: 200694; incorrect!
    # ans: 206780

