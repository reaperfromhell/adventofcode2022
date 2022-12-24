#!/usr/bin/python
# Python3 program to solve adventofcode.com/2022 

best_view = 0

with open("../input/day08.txt") as file_in:
    lines = file_in.readlines()
    for r, line in enumerate(lines):
        for c, tree in enumerate(line.strip()):
            # if r == 0 or r == len(lines)-1 or c == 0 or c == len(line.strip())-1:
            #     visible += 1
            #     continue
            top_visible = 0
            for i in reversed(range(r)): # check top
                if lines[i][c] < tree:
                    top_visible += 1
                else:
                    top_visible += 1
                    break
            left_visible = 0
            for i in reversed(range(c)): # check left
                if lines[r][i] < tree:
                    left_visible += 1
                else:
                    left_visible += 1
                    break
            bottom_visible = 0
            for i in range(r+1,len(lines)): # check bottom
                if lines[i][c] < tree:
                    bottom_visible += 1
                else:
                    bottom_visible += 1
                    break
            right_visible = 0
            for i in range(c+1, len(line.strip())): # check right
                if lines[r][i] < tree:
                    right_visible += 1
                else:
                    right_visible += 1
                    break
            tmp = top_visible * left_visible * right_visible * bottom_visible
            if tmp > best_view:
                best_view = tmp
                    #break #print("Tree r:%s c:%s v:%s is visible from the top."%(r,c,tree))
    print(best_view)