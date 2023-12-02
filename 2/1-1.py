with open("input", "r+") as f:
	data = [l.strip() for l in f.readlines() if l.strip()]

gsum = 0
for l in data:
	cubes = {"red": 0, "green": 0, "blue": 0, "valid": True}
	for sets in l.split(': ')[1].split("; "):
		for hand in sets.split(', '):
			cubes[hand.split(" ")[1]] = int(hand.split(" ")[0])
		if cubes["red"] > 12 or cubes["green"] > 13 or cubes["blue"] > 14:
			cubes["valid"] = False;
	if cubes["valid"]:
		gsum += int(l.split(":")[0].split(" ")[1])

print(gsum)