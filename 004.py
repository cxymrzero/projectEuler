#! usr/bin/env python

def is_pld(num):
    'Test whether a num is a palindrome num'
    numstr = str(num)
    numstr = numstr[::-1] #reverse the string
    newnum = int(numstr)

    if num == newnum:
        return True
    else:
        return False

if __name__ == '__main__':
    lst = []

    for i in range(900, 1000):
        for j in range(900, 1000):
            if is_pld(i*j):
                lst.append(i*j)

    print max(lst)
