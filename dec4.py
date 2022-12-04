"""
Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).

For example, consider the following list of section assignment pairs:

2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
For the first few pairs, this list means:

Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
The Elves in the second pair were each assigned two sections.
The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.
This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:

.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8

Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.

"""


part = 2

import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "dec4_input.txt"))
lines = f.read().splitlines()

def bounds(section):
    # take in a string.
    # return a list of ints.
    section_bounds = section.split('-')
    return int(section_bounds[0]), int(section_bounds[1])

# Part 1
# In how many assignment pairs does one range fully contain the other?
if part == 1:
    # method:
    # for each line, there are two different sections seperated by a comma, so split there.
    # then for each section, there are an upper bound and a lower bound seperated by a dash, so split there.
    # finally, check if one of the sections' upper bound and lower bound are contained by the upper and lower bound of the other section.
    # if they are, then add 1 to the total.
    total = 0
    for line in lines:
        sections = line.split(',')
        section1, section2 = bounds(sections[0]), bounds(sections[1])

        if (section1[0] <= section2[0] and section1[1] >= section2[1]) or (section2[0] <= section1[0] and section2[1] >= section1[1]):
            total += 1

    print(total)
    # ans: 595
    
# Part 2
# It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.
# In how many assignment pairs do the ranges overlap?
elif part == 2:
    # method:
    # once we have the ranges, we now have to check whether the ranges have any overlap rather whether they are contained.
    # e.g. 10-20, 15-25
    # e.g. 20-30, 15-22
    # here there is overlap. We can see that there is overlap if the (upper bound of section1 > lower bound of section2) and (lower bound of section 1 < lower bound of section 2)
    # or vice versa
    total = 0
    for line in lines:
        sections = line.split(',')
        section1, section2 = bounds(sections[0]), bounds(sections[1])

        # print(section1)
        # print(section2)

        if (section1[1] >= section2[0] and section1[0] <= section2[0]) or (section2[1] >= section1[0] and section2[0] <= section1[0]):
            total += 1

    print(total)
    # ans: 952


f.close()