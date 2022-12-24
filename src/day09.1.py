#!/usr/bin/python
# Python3 program to solve adventofcode.com/2022 

path = {(0,0)}
H = (0,0)
T = (0,0)

def move_tail(H, T):
	if H[1]-T[1] > 1: # head moves right
		return (T[0]+(H[0]-T[0]), T[1]+1)

	if H[1]-T[1] < -1:# head moves left
		return (T[0]+(H[0]-T[0]), T[1]-1)

	if H[0]-T[0] > 1: # head move up
		return (T[0]+1, T[1]+(H[1]-T[1]))

	if H[0]-T[0] < -1: # head move down
		return (T[0]-1, T[1]+(H[1]-T[1]))
	return T

with open("../input/day9.txt") as file_in:
    for line in file_in:
        d, c = line.strip().split(" ")
        for i in range(int(c)):
        	if d == 'U': #up
        		H = (H[0]+1,H[1])
        	if d == 'L': #left
        		H = (H[0],H[1]-1)
        	if d == 'D': #down
        		H = (H[0]-1,H[1])
        	if d == 'R': #right
        		H = (H[0],H[1]+1)
        	T = move_tail(H, T)
        	if not set(T).issubset(path):
        		path.add(T)
    print(len(path))
