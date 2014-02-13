#! usr/bin/env python
from math import sqrt

num = 600851475143
max = int(sqrt(600851475143))
div = 3
lst = []

while div <= max:
    while num%div == 0:
        lst.append(div)
        num = num/div
    div += 2

print lst
