
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "dec11_input.txt"))
lines = f.read().splitlines()

part = 2


# method:
# read in a monkey, seperated by empty lines

"""
Monkey 0


"""
class Monkey():
    def __init__(self, items, opType, opNum, testMod, truePass, falsePass):
        self.items = items
        self.opType = opType
        self.opNum = opNum
        self.testMod = testMod
        self.truePass = truePass
        self.falsePass = falsePass
        self.inspections = 0

def makeMonkeys():
    monkeys = []

    items = []
    opType = ""
    opNum = 0
    testMod = 0
    truePass = 0
    falsePass = 0

    for line in lines:
        if line == "":
            # fill in new monkey with gathered info
            newMonkey = Monkey(items, opType, opNum, testMod, truePass, falsePass)
            monkeys.append(newMonkey)
        elif "Starting" in line:
            items = line[18:].split(",")
            items = [int(elem.strip()) for elem in items]
        elif "Operation" in line:
            if "*" in line:
                opType = "MULT"
            elif "+" in line:
                opType = "ADD"
            opNum = line.split(" ")[-1]
        elif "Test" in line:
            testMod = int(line.split(" ")[-1])
        elif "true" in line:
            truePass = int(line.split(" ")[-1])
        elif "false" in line:
            falsePass = int(line.split(" ")[-1])

    newMonkey = Monkey(items, opType, opNum, testMod, truePass, falsePass)
    monkeys.append(newMonkey)

    return monkeys

monkeys = makeMonkeys()

# Part 1
# 
if part == 1:

    # the monkeys pass your the stuff around for 20 rounds
    rounds = 20    
    for i in range(0, rounds):
        for monkey in monkeys:
            while monkey.items:
                # print("item!")
                monkey.inspections += 1
                item = monkey.items[0]
                del monkey.items[0]

                if monkey.opType == "ADD":
                    if monkey.opNum == "old":
                        item = item + item
                    else:
                        item = item + int(monkey.opNum)
                elif monkey.opType == "MULT":
                    if monkey.opNum == "old":
                        item = item * item
                    else:
                        item = item * int(monkey.opNum)
                item = item // 3

                if item % monkey.testMod == 0:
                    monkeys[monkey.truePass].items += [item]
                else:
                    monkeys[monkey.falsePass].items += [item]

    # after 20 rounds,
    # return the product of the number of inspections made by the most inspectious monkeys
    high1 = 0
    high2 = 0

    for monkey in monkeys:
        # print(monkey.inspections)
        if monkey.inspections > high1:
            high2 = high1
            high1 = monkey.inspections                   
        elif monkey.inspections > high2:
            high2 = monkey.inspections

    monkeyBusiness = high1 * high2

    print(monkeyBusiness)
    # ans: 110264






# Part 2
# worry level is no longer divided by 3 each time.
# the number of rounds is now 10000
elif part == 2:
    # the monkeys pass your the stuff around for 20 rounds
    rounds = 10000    
    for i in range(0, rounds):
        for monkey in monkeys:
            while monkey.items:
                # print("item!")
                monkey.inspections += 1
                item = monkey.items[0]
                del monkey.items[0]

                if monkey.opType == "ADD":
                    if monkey.opNum == "old":
                        item = item + item
                    else:
                        item = item + int(monkey.opNum)
                elif monkey.opType == "MULT":
                    if monkey.opNum == "old":
                        item = item * item
                    else:
                        item = item * int(monkey.opNum)

                if item % monkey.testMod == 0:
                    monkeys[monkey.truePass].items += [item]
                else:
                    monkeys[monkey.falsePass].items += [item]

    # after rounds,
    # return the product of the number of inspections made by the most inspectious monkeys
    high1 = 0
    high2 = 0

    for monkey in monkeys:
        # print(monkey.inspections)
        if monkey.inspections > high1:
            high2 = high1
            high1 = monkey.inspections                   
        elif monkey.inspections > high2:
            high2 = monkey.inspections

    monkeyBusiness = high1 * high2

    print(monkeyBusiness)
    # ans: 28497643356


f.close()