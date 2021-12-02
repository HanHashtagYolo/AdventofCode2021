import os

file = open("Day1Input.txt")

depths = []
for line in file:
	depths.append(int(line.strip()))
file.close()

windows = []
increases = 0
for i in range(1, len(depths)-1):
	windows.append([depths[i-1],depths[i],depths[i+1]])

for i in range(1, len(windows)):
	if sum(windows[i-1])<sum(windows[i]):
		increases = increases + 1
print increases