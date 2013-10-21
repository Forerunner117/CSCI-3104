#! /usr/bin/python

import sys

print "fib(" + sys.argv[1] + "):"

n = int(sys.argv[1])
x=[0,1]

if n == 0:
    print 0
    exit()

for i in range(2, n+1):
    x.append(x[i-1] + x[i-2])

print x[n]


