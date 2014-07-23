# It's a simple combination

def arrange(m, n):
    if n == 1:
        return m
    return (m-n+1) * arrange(m, n-1)

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

def combine(m, n):
    return arrange(m, n) / fac(n)

#print combine(5, 3)
#print combine(6, 2)
print combine(40, 20)
