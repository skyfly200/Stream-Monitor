import time

def checkSkips(skips, limit, r):
    count = 0
    t = time.time()
    for s in skips:
        if (t - s[1]) <= r:
            count += 1
    print count
    return count >= limit
