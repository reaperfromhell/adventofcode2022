#!/usr/bin/python
# Python3 program to solve adventofcode.com/2022 

all_calories = []
tmp_calories = 0

with open("../input/day1.txt") as file_in:
    for line in file_in:
        if line == '\n':
            all_calories.append(tmp_calories)
            tmp_calories = 0
            continue
        tmp_calories += int(line)
all_calories.sort()
print(sum(all_calories[-3:]))