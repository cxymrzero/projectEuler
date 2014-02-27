#! usr/bin/env python
from math import sqrt

for i in xrange(1000000):
    s = (i+1)*(i+2)/2
    divs = 0
    for j in xrange(int(sqrt(s))):
        if s%(j+1) == 0:
            divs += 1
    if divs > 250:
        print s
        break

