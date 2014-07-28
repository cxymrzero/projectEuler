import time

start = time.time()

f = open('names.txt', 'r')
content = f.read()
f.close()

content.replace('"', '')
content = content.split(',')
content.sort() 
l = len(content)

def value(s):
	s.split()
	res = 0
	for i in s:
		res += 1 + (int(i) - int('a'))
	return res

score = 0
for i in xrange(1, l+1):
	score += value(content[i-1]) * i

t = time.time() - start
print "find %s in %s secondes" % (score, t)