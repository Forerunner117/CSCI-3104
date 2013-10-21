#! /usr/bin/python
import sys
import random
import longo

def isPrime(N):
	isPrime = True #true until proven not prime!
	counter = 1

	while(isPrime == True):
		rand = random.randint(1, N-1)

		if(longo.logExp(rand, N-1, N) != 1):
			isPrime = False

		counter += 1
		if(counter == 100):
			break	
			
			
	return isPrime

print(isPrime(10))
