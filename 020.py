def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

def sumDigits(n):
    s = 0
    while(n):
        l = n % 10
        s += l
        n = n / 10
    return s

print sumDigits(fac(100))
