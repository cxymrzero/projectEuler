#! usr/bin/env python

lst = [2, 3]
i = 5
while i < 2000000:
    isPrime = True
    for div in range(3, int(i**0.5+1)):
        if i%div == 0:
            isPrime = False
            break
    if isPrime:
        lst.append(i)
    i += 2

print sum(lst)
