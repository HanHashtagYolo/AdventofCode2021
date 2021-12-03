import os

file = open("Day2Input.txt")

hor = 0
vert = 0
for line in file:
	direction, amt = line.strip().split(' ')
	amt = int(amt)
	if direction == 'forward':
		hor = hor + amt
	if direction == 'down':
		vert = vert + amt
	if direction == 'up':
		vert = vert - amt

print hor * vert
