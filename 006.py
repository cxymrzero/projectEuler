#! usr/bin/env python
num1 = num2 = 0
for i in range(1, 101):
    num1 += i*i
    num2 += i
num2 = num2 * num2
print num2 - num1
