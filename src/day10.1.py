#!/usr/bin/python
# Python3 program to solve adventofcode.com/2022 

checkpoints = [20, 60, 100, 140, 180, 220]
res = 0

with open("../input/day10.txt") as file_in:
    x = 1
    cycle = 1
    for instruction in file_in:
        if cycle in checkpoints:
            print(f"BN: After {cycle} cycles, X is {x} = "+ str(x* cycle))
            res += x * cycle
        cycle += 1
        if instruction == "noop":
            continue
        elif instruction.startswith("addx"):
            if cycle in checkpoints:
                print(f"AA: After {cycle} cycles, X is {x} = "+ str(x* cycle))
                res += x * cycle
            cycle += 1  # Increment cycle for addx instruction
            _, value = instruction.split()
            x += int(value)

    print(f"After {cycle} cycles, X is {x}")
    print(res)