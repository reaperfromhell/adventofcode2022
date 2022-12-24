#!/usr/bin/python
# Python3 program to solve adventofcode.com/2022 

path = [(0,0)]
R = [(0,0)]*10

def clamp(n):
    return max(min(1, n), -1)

def move_knot(H, T):
	if H[1]-T[1] > 1: # head moves right
		return (T[0]+clamp((H[0]-T[0])), T[1]+1)

	if H[1]-T[1] < -1:# head moves left
		return (T[0]+clamp((H[0]-T[0])), T[1]-1)

	if H[0]-T[0] > 1: # head move up
		return (T[0]+1, T[1]+clamp((H[1]-T[1])))

	if H[0]-T[0] < -1: # head move down
		return (T[0]-1, T[1]+clamp((H[1]-T[1])))
	return T

with open("../input/day9.txt") as file_in:
    for line in file_in:
        d, c = line.strip().split(" ")

        for i in range(int(c)):
        	if d == 'U': #up
        		R[0] = (R[0][0]+1,R[0][1])
        	if d == 'L': #left
        		R[0] = (R[0][0],R[0][1]-1)
        	if d == 'D': #down
        		R[0] = (R[0][0]-1,R[0][1])
        	if d == 'R': #right
        		R[0] = (R[0][0],R[0][1]+1)
        	for i in range(1,10):
        		R[i] = move_knot(R[i-1], R[i])
        	if not R[9] in path:
        		path.append(R[9])
    print(len(path))
