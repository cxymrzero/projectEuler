#!/usr/bin/env python
#-*-coding:utf-8-*-
import time

limit = 1000000

def collatz(n, cnt=1):
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
        cnt += 1
    return cnt

start = time.time()
max = [0, 0] # max[0]:number, max[1]:length
for i in xrange(limit):
    c = collatz(i)
    if c > max[1]:
        max[0] = i
        max[1] = c

elapsed = time.time() - start
print "Answer is %d, length %d in %s" % (max[0], max[1], elapsed)
