#! usr/bin/env python

sum = 5 #2+3
i = 5
while i < 2000000:
    isPrime = True
    for div in xrange(3, int(i**0.5+1)):
        if i%div == 0:
            isPrime = False
            break
    if isPrime:
        sum += i
    i += 2

print sum
