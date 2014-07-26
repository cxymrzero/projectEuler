m = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
d_leap = {}

for i in range(1901, 2001):
    d_leap[i] = True if i%4==0 and i%100!=0 or i%400==0 else False

res = 0
cnt = -4 # Jan 1st, 1901 is Mon.
for i in range(1901, 2001):
    for j in range(12):
        if j != 1:
            cnt += m[j]
        else:
            cnt += 29 if d_leap[i] else 28
#        print cnt
        cnt = cnt % 7
        if cnt == 0:
            res += 1

print res
#print d_leap
