#! /usr/bin/python
import sys
import longo

M = 808017424794512875886459904961710757005754368000000000

#Take user input. Defaults to M^M%2013
if len(sys.argv) > 1:
	x = int(sys.argv[1])
	x_copy = x
	y = int(sys.argv[2])
	y_copy = y
	N = int(sys.argv[3])
else: 
	x = M
	x_copy = x
	y = M
	y_copy = y
	N = 2013

ans = longo.logExp(x, y, N)

#acc = 1

#while (y!=0):
#	if 1 & y: #if true, y is odd
#		acc = (acc*x)%N
#	x = (x*x)%N
#	y>>=1

print str(ans)


#print an appropriate response
#if len(sys.argv) > 1:
#	print str(x_copy) + "^(" + str(y_copy) + ") % " + str(N) + " = " + str(acc)
#else:
#	print "M^(M) % 2013 = " + str(acc)