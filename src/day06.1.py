#!/usr/bin/python
# Python3 program to solve adventofcode.com/2022 

with open("../input/day6.txt") as file_in:
    line = file_in.readline()
    for i, char in enumerate(line):
        check = set(line[i:i+4])
        if( len(check) == 4 ):
          print(check)
          print(i+4)
          break