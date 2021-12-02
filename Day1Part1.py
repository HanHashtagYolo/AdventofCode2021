import os

file = open("Day1Input.txt")

depths = []
for line in file:
	depths.append(int(line.strip()))
file.close()

increases = 0
for i in range(1, len(depths)):
	if depths[i-1]<depths[i]:
		increases = increases + 1

print increases, depths[i]