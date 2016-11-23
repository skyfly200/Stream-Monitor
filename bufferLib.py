def checkSkips(r):
	count = 0
	for s in skips:
		if (time.time() - s[1]) <= r:
			count += 1
	return count > skipLimit
