#! usr/bin/env python

lst = [1, 1]
sum = 0
while 1:
    lst.append(lst[-1]+lst[-2])
    if lst[-1] > 4000000:
        break
    if lst[-1]%2 == 0:
        sum += lst[-1]

print sum
