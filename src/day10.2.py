#!/usr/bin/python
# Python3 program to solve adventofcode.com/2022 

crt = [['.'] * 40 for _ in range(6)]

with open("../input/day10.txt") as file_in:
    x = 1
    cycle = 1
    for instruction in file_in:
        div = divmod(cycle-1, 40)
        if div[1] in range(x-1,x+2):
            crt[div[0]][div[1]] = '#'
        cycle += 1
        if instruction == "noop":
            continue
        elif instruction.startswith("addx"):
            div = divmod(cycle-1, 40)
            if div[1] in range(x-1,x+2):
                crt[div[0]][div[1]] = '#'
            cycle += 1  # Increment cycle for addx instruction
            _, value = instruction.split()
            x += int(value)
for i in crt:
    print(''.join(i))