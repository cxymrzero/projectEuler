limit = 20
cache = [0] * limit # Use cache to save the caculated answers
#cache[i] stores d(i+1)!

def d(n):
    s = 0 
    for i in reversed(xrange(n-1)):
        if n % (i+1) == 0:
            if cache[i]!=0:
                return s + i+1 #here the num is i+1
            else:
                s += i+1
    return s

# d(0) = d(1) = 0
cache[1] = 1 # d(2) = 1
for i in xrange(limit):
    if i<3: continue #cache[0->1] is known
    cache[i-1] = d(i)

res = []
for i in xrange(limit):
    if cache[i] == cache[cache[i]]:
        res.append(i+1)
        print cache[i]

print res
print d(3)
