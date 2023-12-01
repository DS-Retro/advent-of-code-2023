with open("input", "r+") as f:
	data = [l.strip() for l in f.readlines() if l.strip()]

ts = []
for l in data:
	cn = ""
	for c in l:
		try:
			n = int(c)
			cn += str(n)
		except:
			continue
	ts.append(int(cn[0] + cn[-1]))

print(sum(ts))