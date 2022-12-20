#!/usr/bin/python
# Python3 program to solve adventofcode.com/2022 

max_calories = 0
tmp_calories = 0

with open("../input/day1.txt") as file_in:
    for line in file_in:
        if line == '\n':
            if tmp_calories > max_calories:
                max_calories = tmp_calories
            tmp_calories = 0
            continue
        tmp_calories += int(line)
print(max_calories)