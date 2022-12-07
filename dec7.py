"""
The filesystem consists of a tree of files (plain data) and directories (which can contain other directories or files). The outermost directory is called /. You can navigate around the filesystem, moving into or out of directories and listing the contents of the directory you're currently in.

Within the terminal output, lines that begin with $ are commands you executed, very much like some modern computers:

cd means change directory. This changes which directory is the current directory, but the specific result depends on the argument:
cd x moves in one level: it looks in the current directory for the directory named x and makes it the current directory.
cd .. moves out one level: it finds the directory that contains the current directory, then makes that directory the current directory.
cd / switches the current directory to the outermost directory, /.
ls means list. It prints out all of the files and directories immediately contained by the current directory:
123 abc means that the current directory contains a file named abc with size 123.
dir xyz means that the current directory contains a directory named xyz.

To begin, find all of the directories with a total size of at most 100000, then calculate the sum of their total sizes. In the example above, these directories are a and e; the sum of their total sizes is 95437 (94853 + 584). (As in this example, this process can count files more than once!)

"""


part = 2

import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "dec7_input.txt"))
lines = f.read().splitlines()

class Dir():
    def __init__(self, parent):
        self.parent = parent
        self.children = {}
        self.dirSize = 0
    def add_child_dir(self, childName, childDir):
        self.children[childName] = childDir
    def add_file(self, fileStr):
        fileComponents = fileStr.split(" ")
        # print(fileComponents)
        self.dirSize += int(fileComponents[0])
    def calculate_size(self):
        # return the size of yourself and all your children
        # and your children's children, etc...
        total = self.dirSize
        explore = set(list(self.children.values()).copy())
        while explore:
            cur = explore.pop()
            # add all their own children to explore set
            for dirRef in list(cur.children.values()):
                explore.add(dirRef)
            # add their size to total
            total += cur.dirSize
        return total

# Part 1
# Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
if part == 1:
    # method:
    # read in each line. Depending on how the line starts:
    # -$: either cd or ls. 
    #       If cd .. go to parent of scope, 
    #       if cd isalpha() then create a new Dir object, update children, and switch to new dir's scope. 
    #       If ls, do nothing.
    # -dir: add this dir to the children of the current dir
    # -isdigit(): it's a file, so add its size to the current dir
    # *note: the size of a dir if counted as part of the size of its parent dir.
    # finally, once we've read the whole file, then we calculate the total sizes of each dir and calc the sum of all with size <= 100000.

    home = Dir(None)
    scope = home

    for line in lines[1:]:
        # print(line)

        if line[:4] == "$ cd":
            if line[5:] == "..":
                # go to parent's scope
                # print("moving to parent dir")
                scope = scope.parent

            else:
                # move to this dir in scope's children
                # print("move to new scope")
                moveName = line[5:]
                # print("moving to dir named " + moveName)
                scope = scope.children[moveName]
            
        elif line[:4] == "$ ls":
            continue

        elif line[:3] == "dir":
            # add new dir to scope's children
            # print("create and add new dir")
            childName = line[4:]
            newDir = Dir(scope)
            scope.add_child_dir(childName, newDir)
            
        else:
            # add new file to scope's size
            # print(line)
            # print("^add file to scope")           
            scope.add_file(line)

    # we've finished constructing the file tree, now we gather the sum of sizes dirs whose own size <= 100000
    # *remember: the size of a child dir counts as part of your own size.

    # homeSize = home.calculate_size()
    # print(homeSize)

    explore_dirs = set()
    explore_dirs.add(home)
    total = 0
    while explore_dirs:
        cur = explore_dirs.pop()

        # add all their own children to explore set
        for dirRef in list(cur.children.values()):
            explore_dirs.add(dirRef)
        # add their size to total
        curSize = cur.calculate_size()
        if curSize <= 100000:
            total += curSize

    print(total)
    # ans: 1490523
    

# Part 2
# The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. 
# You need to find a directory you can delete that will free up enough space to run the update.
# Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
elif part == 2:
    # method:
    # the good news is that we only need to delete one dir. 
    # essentially, find the dir with the smallest size that is still greater than (70000000 - home dir size)
    # explore all the directorys and keep a running minimum directory that still follows the constraints
    home = Dir(None)
    scope = home

    for line in lines[1:]:
        # print(line)

        if line[:4] == "$ cd":
            if line[5:] == "..":
                # go to parent's scope
                # print("moving to parent dir")
                scope = scope.parent

            else:
                # move to this dir in scope's children
                # print("move to new scope")
                moveName = line[5:]
                # print("moving to dir named " + moveName)
                scope = scope.children[moveName]
            
        elif line[:4] == "$ ls":
            continue

        elif line[:3] == "dir":
            # add new dir to scope's children
            # print("create and add new dir")
            childName = line[4:]
            newDir = Dir(scope)
            scope.add_child_dir(childName, newDir)
            
        else:
            # add new file to scope's size
            # print(line)
            # print("^add file to scope")           
            scope.add_file(line)

    homeSpace = home.calculate_size()
    currentFreeSpace = 70000000 - homeSpace
    sizeToDelete = 30000000 - currentFreeSpace
    # print(sizeToDelete)
    
    explore_dirs = set()
    for dirRef in list(home.children.values()):
        explore_dirs.add(dirRef)
    minDir = homeSpace
    while explore_dirs:
        cur = explore_dirs.pop()

        # add all their own children to explore set
        for dirRef in list(cur.children.values()):
            explore_dirs.add(dirRef)
        # add their size to total
        curSize = cur.calculate_size()
        if curSize >= sizeToDelete and curSize < minDir:
            minDir = curSize
    print(minDir)
    # ans: 12390492

f.close()