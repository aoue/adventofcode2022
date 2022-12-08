"""
We read in a file of format something like this:
30373
25512
65332
33549
35390

Each digit is a single tree of height 0-9. We must determine how many trees are visible.
A tree is not visible if:
-it is not on the edge
and
-at least one tree in a straight line between it and each of the four edges has a height greater than it.
"""


part = 2

import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "dec8_input.txt"))
lines = f.read().splitlines()

def isVisible(grid, row_num, col_num, row, col):
    # method:
    # -so we have to check on the tree moving in from each edge.
    # -at each tree we encounter along the way, if that tree's height is greater/eq than our tree's height, 
    #  then we know the tree is not visible from that direction and can stop.
    # -if we make it all the way to our tree, then we can return True.
    # -if we don't make it to the tree from any direction, return False.

    tree = grid[row][col]
    
    # from the left edge going to the right
    for i in range(0, col + 1):
        # print(grid[row][i])
        if i == col:
            return True
        if grid[row][i] >= tree:
            break
    # from the right edge going to the left
    for i in range(col_num-1, col-1, -1):
        if i == col:
            return True
        if grid[row][i] >= tree:
            break
    # from the top edge going to the bottom
    for i in range(0, row + 1):
        if i == row:
            return True
        if grid[i][col] >= tree:
            break
    # from the bottom edge going to the top
    for i in range(row_num-1, row-1, -1):
        # print(grid[i][col])
        if i == row:
            return True
        if grid[i][col] >= tree:
            break

    return False

def scenicScore(grid, row_num, col_num, row, col):
    # method:
    # -starting from the tree in question, go as far as you can is each direction until your view is blocked, counting the total number of trees seen (including the blocking tree)
    # -return the product

    tree = grid[row][col]
    rightScore, leftScore, topScore, bottomScore = 0, 0, 0 ,0

    # from the tree going to the right
    for i in range(col + 1, col_num):
        # print(grid[row][i])
        rightScore += 1
        if tree <= grid[row][i]:
            break
    # print("right = " + str(rightScore))
    # from the tree going to the left
    for i in range(col-1, -1, -1):
        # print(grid[row][i])
        leftScore += 1
        if tree <= grid[row][i]:
            break
    # print("left = " + str(leftScore))

    # from the tree going to the bottom
    for i in range(row + 1, row_num):
        # print(grid[i][col])
        bottomScore += 1
        if tree <= grid[i][col]:
            break

    # print("bottom = " + str(bottomScore))
    # from the tree going to the top
    for i in range(row-1, -1, -1):
        # print(grid[i][col])
        topScore += 1
        if tree <= grid[i][col]:
            break
    # print("top = " + str(topScore))

    return rightScore * leftScore * topScore * bottomScore

# Part 1
# Consider your map; how many trees are visible from outside the grid?
# *note: all edge trees are visible by default
if part == 1:
    # method:
    # read in and split into a grid pattern where each element is a 1-digit int.
    # once constructed, check the visibility of each tree.
    grid = []
    for line in lines:
        # print(line)
        components = [int(x) for x in list(line)]
        grid.append(components)

    # *note: indexing into grid, first index is row, second index is column.
    row_num = len(grid)
    col_num = len(grid[0])

    total = (2 * (row_num-1)) + (2 * (col_num-1))
    # print(total)
    for row in range(1, row_num-1):
        for col in range(1, col_num-1):
            if isVisible(grid, row_num, col_num, row, col):
                # print("the tree as " + str(row) + ", " + str(col) + " is visible")
                total += 1

    print(total)
    # ans: 1840

# Part 2
# For a tree, the scenic score is the number of trees it can see in each direction, multiplied together.
# Consider each tree on your map. What is the highest scenic score possible for any tree? 
elif part == 2:
    # method:
    # for each tree, calculate the scenic score. Return the max scenic score.
    # *note: since the trees on the edge have 0 trees seen in a direction, don't need to check them.
    grid = []
    for line in lines:
        # print(line)
        components = [int(x) for x in list(line)]
        grid.append(components)

    # *note: indexing into grid, first index is row, second index is column.
    row_num = len(grid)
    col_num = len(grid[0])

    bestScenicScore = -1
    for row in range(1, row_num-1):
        for col in range(1, col_num-1):
            score = scenicScore(grid, row_num, col_num, row, col)
            if score > bestScenicScore:
                # print("the tree as " + str(row) + ", " + str(col) + " is visible")
                bestScenicScore = score
    
    print(bestScenicScore)
    # ans: 405769

f.close()