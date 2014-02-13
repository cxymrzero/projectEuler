#! usr/bin/env python

lst = [2, 3]
num = 5
while len(lst) <= 10000: #10000!
    isPrime = True
    for i in lst:
        if num % i == 0:
            isPrime = False
            break

    if isPrime:
        lst.append(num)
    num += 2

print lst[-1]
