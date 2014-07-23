#-*- coding: utf-8 -*-
import time
'''
By using dynamic programming, I save all the caculated answer to the list cache.
And simply drop all the nums that larger than the limit.
I tried to save all the BIG nums to a dict, but that makes it even SLOWER!
'''

start = time.time()
limit = 1000000
#limit = 10
cache = [0] * limit
cache[1] = 1

def collatz(num, cnt=0):
    while num > 1:
        if num < limit and cache[num]:
            return cnt+cache[num]
        cnt += 1
        if num % 2 == 0:
            num = num / 2
        else:
            num = num*3 + 1
    return cnt

max = [0, 0]

for i in xrange(limit):
    c = collatz(i)
    cache[i] = c
    if c > max[1]:
        max[0] = i
        max[1] = c
#    print i, c

elapsed = time.time() - start
print "answer: %d, length: %d, time: %s" % (max[0], max[1], elapsed)
