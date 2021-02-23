import os
import sys
from array import *
import numpy as np
from collections import OrderedDict 
import pprint
import json
sys.setrecursionlimit(5000)
#global grid
grid = []
print("hello world")

#open file




######################################################################
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None



######################
sumArray = []
sumDict = OrderedDict() 
print(os.path.join(sys.path[0], 'sudoku.txt'))
reader = open(os.path.join(sys.path[0], 'sudoku.txt'))
try:
    i = 0
    for line in reader.readlines():
        if line[0] == 'G':
            print('Puzzle '+ line.strip())
            puzzleName = line.strip()
        #print line,
        if line[0] != 'G':
            row = line
            #row = line.split()
            line = " ".join(line)
            row = line.split()
            row = map(int, row)
            grid.append(row)
            print row

            if len(grid) == 9 :
                solve(grid)
                print("-=Solution=-\n")
                print(np.matrix(grid))
                sum = grid[0][0]+grid[0][1]+grid[0][2]
                sumArray.append(sum)
                sumDict.update({puzzleName :sum})
                print('===>' + str(sum))
                del grid[:]
                print ('-----------------------------------------')
    #for i in range(9):
    #    print(i)

finally:
    reader.close()


print(sumArray)

pp = pprint.PrettyPrinter(indent=4, width=1)
#pp.pprint(sumDict)
print(json.dumps(sumDict, indent=4, sort_keys=True))

#print_board(grid)
# print(np.matrix(grid))
# solve(grid)
# print("___________________")
# print(np.matrix(grid))
# sum = grid[0][0]+grid[0][1]+grid[0][2]
# print('===>' + str(sum) )
