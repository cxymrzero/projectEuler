#! usr/bin/env python

breakout = False
for a in range(1, 333):
    if breakout:
        break
    for b in range(a+1, 1000):
        if a*a+b*b == (1000-a-b)**2:
            print a*b*(1000-a-b)
            breakout = True
            break
