n = int(input("input n\n"))
robots = {}

for _ in range(n):
	s, z = map(int, input("input s and z\n").split())
	robots[s] = z

max_s = max(robots.keys())
max_z = max(robots.values())

if robots[max_s] == max_z:
	print("NIE")
else:
	print("TAK")