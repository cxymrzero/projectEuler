def addPow(exp):
    lst = list(str(2 ** exp))
    sum = 0
    for i in lst:
        sum += int (i)
    return sum

print addPow(1000)
