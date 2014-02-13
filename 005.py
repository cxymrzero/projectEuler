#! usr/bin/env python

lst = [2, 3]
for i in range(5, 21):
    isnew = True
    for div in lst:
        if i%div == 0 or i in lst:
            isnew = False
    if isnew:
        lst.append(i)

s = 1
for i in lst:
    s *= i
s *= 8*3
print s
