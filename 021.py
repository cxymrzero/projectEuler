# Brute force, tried cache the counted nums but failed :(
import time
start = time.time()

limit = 10000

def d(n):
    s = 0
    for i in xrange(1, n):
        if n%i == 0:
            s += i
    return s

divSum = []
for i in xrange(1, limit+1):
    divSum.append(d(i))

res = 0
for i in xrange(limit):
    sum_i = divSum[i]
    if sum_i<=limit and sum_i>0 and i+1==divSum[sum_i-1] and i!=sum_i-1:
        res += i+1

elapsed = time.time() - start

print "%s found in %s seconds" % (res, elapsed)
