

#hw3_num5.py
#Austin Longo
#9/26/13

#! /usr/bin/python
import sys
import longo #collection of frequently used custom functions

acc = 0

for i in range(1, 1000):
	x = longo.random_n_digit(100)
	acc += (longo.next_prime(x) - x)

print acc/1000



'''
Sample Output:
--------------

225

'''