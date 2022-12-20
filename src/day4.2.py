#!/usr/bin/python
# Python3 program to solve adventofcode.com/2022 
overlaps = 0

def calculate_overlaps(line):
    elf1, elf2 = line.split(",")
    r1,r2 = elf1.split("-")
    range1 = range(int(r1),int(r2)+1)
    r1,r2 = elf2.split("-")
    range2 = range(int(r1),int(r2)+1)

    if set(range1).intersection(range2):
        return 1
    else:
        return 0
    return 0

with open("../input/day4.txt") as file_in:
    for line in file_in:
            overlaps += calculate_overlaps(line)
print(overlaps)
