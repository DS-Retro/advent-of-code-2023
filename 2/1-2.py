with open("input", "r+") as f:
	data = [l.strip() for l in f.readlines() if l.strip()]

gsum = 0
for l in data:
	cubes = {"red": 0, "green": 0, "blue": 0, "valid": True}
	for sets in l.split(': ')[1].split("; "):
		for hand in sets.split(', '):
			cubes[hand.split(" ")[1]] = max(int(hand.split(" ")[0]), int(cubes[hand.split(" ")[1]]))
	gsum += cubes['red'] * cubes['green'] * cubes['blue']

print(gsum)