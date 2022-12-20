#!/usr/bin/python
# Python3 program to print 
# given matrix in spiral form 

total_prio = 0

#A = ROCK = 1 = X
#B = PAPER = 2 = Y
#C = SCISSORS = 3 = Z 

def calculate_prio(line):
    #print(line, int((len(line)-1) / 2))
    comp1 = line[:int((len(line)-1) / 2)]
    comp2 = line[int((len(line)-1) / 2):]
    error = set(comp1).intersection(comp2).pop()
    if error.isupper():
        return ord(error)-38 #ASCII offset for uppercase leters
    else:
        return ord(error)-96 #ASCII offset for lowercase letters
    return 0

with open("../input/day3.txt") as file_in:
    for line in file_in:
        total_prio += calculate_prio(line)
print(total_prio)
