#!/usr/bin/python
# Python3 program to solve adventofcode.com/2022 

with open("../input/day05.txt") as file_in:
    file = file_in.readlines()
    n = len(file[0])           # length of each container line
    containers = []
    for i in range(int(n/4)):
        containers.append([])  # build container matrix
    for i, line in enumerate(file):
        if line[1].isdigit():
            break
        for c in range(0,n,4):
            if line[c+1] != ' ':
                containers[int(c/4)].insert(0,line[c+1])
    for line in file[i+2:]:
        sline = line.strip().split(' ')
        tmp = []
        for l in range(int(sline[1])):
            tmp.insert(0,containers[int(sline[3])-1].pop())
        containers[int(sline[5])-1] += tmp

#print('\n'.join([' '.join([str(cell) for cell in row]) for row in containers]))

result = ''
for i in containers:
    result += i.pop()
print(result)