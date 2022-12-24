#!/usr/bin/python
# Python3 program to solve adventofcode.com/2022 

visible = 0

with open("../input/day8.txt") as file_in:
    lines = file_in.readlines()
    for r, line in enumerate(lines):
        for c, tree in enumerate(line.strip()):
            if r == 0 or r == len(lines)-1 or c == 0 or c == len(line.strip())-1:
                visible += 1
                continue
            is_top_visible = True
            for i in range(r): # check top
                if is_top_visible == True and lines[i][c] >= tree:
                    is_top_visible = False
                    break
            if is_top_visible:
                visible += 1
                continue
            is_left_visible = True
            for i in range(c): # check left
                if is_left_visible == True and lines[r][i] >= tree:
                    is_left_visible = False
                    break
            if is_left_visible:
                visible += 1
                continue
            is_bottom_visible = True
            for i in range(r+1,len(lines)): # check bottom
                if is_bottom_visible == True and lines[i][c] >= tree:
                    is_bottom_visible = False
                    break
            if is_bottom_visible:
                visible += 1
                continue
            is_right_visible = True
            for i in range(c+1, len(line.strip())): # check right
                if is_right_visible == True and lines[r][i] >= tree:
                    is_right_visible = False
                    break
            if is_right_visible:
                visible += 1
                continue #print("Tree r:%s c:%s v:%s is visible from the top."%(r,c,tree))
    print(visible)