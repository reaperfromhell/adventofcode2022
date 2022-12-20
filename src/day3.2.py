#!/usr/bin/python
# Python3 program to solve adventofcode.com/2022 

total_prio = 0

def calculate_prio(lines):
    item = set(lines[0].strip()).intersection(lines[1].strip(),lines[2].strip()).pop() #strip to remove potential spaces as well as newline char
    if item.isupper():
        return ord(item)-38 #ASCII offset for uppercase leters
    else:
        return ord(item)-96 #ASCII offset for lowercase letters
    return 0

with open("../input/day3.txt") as file_in:
    lines = file_in.readlines()
    for i in range(0, len(lines), 3):
            total_prio += calculate_prio(lines[i:i+3])
print(total_prio)
