oneDigit = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', \
        5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}
teen = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', \
        16:"sixteen", 17:'seventeen', 18:'eighteen', 19:'nineteen'}
#FORTY!!
ty = {0:'', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', \
        7:'seventy', 8:'eighty', 9:'ninety'}
default = {'hundred':7, 'and':3}

for d in [oneDigit, teen, ty]:
    for i in d:
        d[i] = len(d[i])

#read two digits
def twoDigits(n):
    up = n / 10
    low = n % 10
    if up == 1:
        return teen[n]
    else:
        return ty[up] + oneDigit[low]

def read(n):
    cnt = 0
    up = n / 100 #hundred
    low = n % 100 #last two digits
    cnt += oneDigit[up]
    if up!=0 and low!=0:
        cnt += default['hundred'] + default['and']
    elif up!=0 and low==0:
        cnt += default['hundred']
    cnt += twoDigits(low)
    return cnt

sum = 0
#while True:
#    i = raw_input("enter a num")
#    print read(int(i))
for i in xrange(1000):
    sum += read(i)
sum += 11 #one thousand

print sum
