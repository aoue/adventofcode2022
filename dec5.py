"""
The input file is split into two sections; the starting stacks and then all the operations performed. The sections are seperated by an emptyline.
We need to first convert the starting stacks into lists. This is helped because the strings are all the same length, meaning that an element at a certain index will always correspond to a certain stack.
All that is needed is to check whether it is blank or not. The stacks will be represented by a list of lists of strings.
"""



part = 2

import re
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "dec5_input.txt"))
lines = f.read().splitlines()

def create_stacks(lines):
    line_length = len(lines[0])
    number_of_stacks = -1
    start_after = 1
    for line in lines:
        start_after += 1
        if line[0] != '[':
            number_of_stacks = int(line[line_length - 2])
            # print(number_of_stacks)
            break
    ret = [[] for i in range(number_of_stacks)]
    for line in lines:
        if '[' not in line:
            break

        # given a line, we have to add 1 item to each stack.
        index_counter = 1
        for stack in ret:
            if (line[index_counter] != ' '):
                stack.append(line[index_counter])
            index_counter += 4
    return ret, start_after



# Part 1
# After the rearrangement procedure completes, what crate ends up on top of each stack?
if part == 1:
    # method:
    # create the stacks in their initial state
    # then read in each operation, which have the form, e.g. 'move 3 from 9 to 4'
    # which means to move the top 3 boxes of stack 9 to the top of stack 4 as if they were moved one at a time (i.e. reverse the list of moved boxes)
    # repeat for operations
    # finally, return a string bearing the concatenation of the top of each stack.
    # note: (the first item in a stack is on top, the last item is on the bottom)
    stacks, start_after = create_stacks(lines)

    for line in lines[start_after:]:
        # if it's an operation line
        if line[0] == 'm':
            # convert the operation into its 3 parts
            info = line.split()
            info = [int(info[i]) for i in range(0, len(info)) if i % 2 == 1]            
            number_to_move = info[0]
            from_where = info[1] - 1
            to_where = info[2] - 1

            # print(number_to_move)
            # print(from_where)
            # print(to_where)
            
            moved = stacks[from_where][:number_to_move]
            moved.reverse()
            stacks[to_where] = moved + stacks[to_where]
            # print(stacks[to_where])

            # finally, remember to remove those boxes from the stack they were stripped from.
            stacks[from_where] = stacks[from_where][number_to_move:]

    top_of_all = ""
    # finally, collect the top box from each list into a return string
    for stack in stacks:
        if stack:
            top_of_all += stack[0]
    print(top_of_all)
    # ans: QNNTGTPFN
    
# Part 2
# What's changed? Crates are now moved all at once (meaning that their order is no longer reversed as they are added to the new stack.)
# It suffices to removed the line 'moved.reverse()' from the part 1 solution.
# After the rearrangement procedure completes, what crate ends up on top of each stack?
elif part == 2:
    # method:
    # all that's changed is that we now no longer reverse the moved crates.
    stacks, start_after = create_stacks(lines)

    for line in lines[start_after:]:
        # if it's an operation line
        if line[0] == 'm':
            # convert the operation into its 3 parts
            info = line.split()
            info = [int(info[i]) for i in range(0, len(info)) if i % 2 == 1]            
            number_to_move = info[0]
            from_where = info[1] - 1
            to_where = info[2] - 1

            # print(number_to_move)
            # print(from_where)
            # print(to_where)
            
            moved = stacks[from_where][:number_to_move]
            stacks[to_where] = moved + stacks[to_where]
            # print(stacks[to_where])

            # finally, remember to remove those boxes from the stack they were stripped from.
            stacks[from_where] = stacks[from_where][number_to_move:]

    top_of_all = ""
    # finally, collect the top box from each list into a return string
    for stack in stacks:
        if stack:
            top_of_all += stack[0]
    print(top_of_all)
    # ans: GGNPJBTTR


f.close()