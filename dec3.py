"""
One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.
Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.
The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).
The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

For example, suppose you have the following list of contents from six rucksacks:
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw

The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
The fourth rucksack's compartments only share item type v.
The fifth rucksack's compartments only share item type t.
The sixth rucksack's compartments only share item type s.
To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.


"""
part = 2

import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "dec3_input.txt"))
lines = f.read().splitlines()

# Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
if part == 1:
    # method:
    # the rugsacks are divided into 2 compartments of equal length, so split each sack (line) into 2 halves.
    # then, compare the halves to find the 1 character that appears in both halves. (how? convert both strings to sets and use set.intersection)
    # then, add the value of that character to the sum.
    # repeat for all lines.
    total = 0
    for line in lines:
        half1 = line[:(len(line)//2)]
        half2 = line[(len(line)//2):]
        common = "".join(set(half1).intersection(set(half2)))

        if common.isupper():
            total += ord(common.lower()) - 70
        else:
            total += ord(common) - 96
    print(total)
    # ans = 7826

# elves are divided into groups of 3
# for each group of 3, the badge is the only item carried by all three elves
# Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
elif part == 2:
    # method:
    # for each 3 lines, find the character in common between the three of them.
    # then add the value of that character to the total.
    total = 0
    for i in range(0, len(lines), 3):
        elf1 = lines[i]
        elf2 = lines[i+1]
        elf3 = lines[i+2]

        common = "".join(set(elf1).intersection(set(elf2).intersection(set(elf3))))
        if common.isupper():
            total += ord(common.lower()) - 70
        else:
            total += ord(common) - 96
    print(total)
    # ans = 2577