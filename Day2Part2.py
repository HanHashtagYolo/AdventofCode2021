import os

file = open("Day2Input.txt")

hor = 0
vert = 0
aim = 0
for line in file:
	direction, amt = line.strip().split(' ')
	amt = int(amt)
	if direction == 'forward':
		hor = hor + amt
		vert = vert + (amt*aim)
	if direction == 'down':
		aim = aim + amt
	if direction == 'up':
		aim = aim - amt

print hor * vert