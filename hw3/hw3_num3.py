

#hw3_num3.py
#Austin Longo
#9/26/13

#! /usr/bin/python
import sys
import longo #collection of frequently used custom functions

found = False
pseudo2 = False
pseudo3 = False
pseudo2013 = False
N = 3

while (found != True):
	if(longo.is_prime(N) == False): #if i is composite
		#test 2-pseudoprime
		if (longo.mod_exp(2, N-1, N) == 1):
			pseudo2 = True

		#test 3-pseudoprime
		if (longo.mod_exp(3, N-1, N) == 1):
			pseudo3 = True

		#test 2013-pseudoprime
		if (longo.mod_exp(2013, N-1, N) == 1):
			pseudo2013 = True

		if(pseudo2 and pseudo3 and pseudo2013):
			found = True
			break

		pseudo2 = False; pseudo3 = False; pseudo2013 = False

	N += 2

print(N)



'''
Sample Output:
--------------

1105

'''