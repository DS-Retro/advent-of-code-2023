
with open("input", "r+") as f:
	data = [l.strip() for l in f.readlines() if l.strip()]

nt = [("zero", 0), ("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5), ("six", 6), ("seven", 7), ("eight", 8), ("nine", 9)]


def ttn(s):
	i = 0
	ns = ""
	tmp = ""
	while i < len(s):
		try:
			ns += str(int(s[i]))
			i += 1
		except:
			tmp += s[i]
			for n in nt:
				if n[0] in tmp:
					ns += str(n[1])
					tmp = tmp[-1]
			i += 1
	return ns

ts = []
for l in data:
	cn = ttn(l)
	ts.append(int(cn[0] + cn[-1]))

print(sum(ts))