#!/usr/bin/python
# Python3 program to solve adventofcode.com/2022  

total_score = 0

#A = ROCK = 1
#B = PAPER = 2
#C = SCISSORS = 3

#X = LOSE
#Y = DRAW
#Z = WIN

def calculate_score(line):
    him, me = line.strip().split(" ")
    #Him A
    if him == 'A' and me == 'X':
        return 0 + 3
    if him == 'A' and me == 'Y':
        return 3 + 1
    if him == 'A' and me == 'Z':
        return 6 + 2
    
    #Him B
    if him == 'B' and me == 'X':
        return 0 + 1    
    if him == 'B' and me == 'Y':
        return 3 + 2    
    if him == 'B' and me == 'Z':
        return 6 + 3
    
    #Him C
    if him == 'C' and me == 'X':
        return 0 + 2
    if him == 'C' and me == 'Y':
        return 3 + 3
    if him == 'C' and me == 'Z':
        return 6 + 1
    
with open("../input/day02.txt") as file_in:
    for line in file_in:
        total_score += calculate_score(line)
print(total_score)
