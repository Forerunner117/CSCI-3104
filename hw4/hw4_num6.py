

#hw4_num6.py
#Austin Longo
#10/03/13

#! /usr/bin/python
import sys
import random
import math

def string_selection(collection, k, recs):
	n = len(collection)
	if(n == 1):
		v = 0
	else:
		v = random.randint(0, n-1)
	pivot = collection[v]
	collectionL = list()
	collectionR = list()
	collectionV = list()

	collectionL = [i for i in collection if i < pivot]
	collectionR = [i for i in collection if i > pivot]

	lenL = len(collectionL)
	lenR = len(collectionR)


	if(k == lenL+1):
		with open("recursions.txt", "a") as myfile:
			myfile.write('{}\n'.format(recs))
		return collection[v]
	elif(k <= lenL):
		return string_selection(collectionL, k, recs+1)		
	elif(k > lenL+1):
		return string_selection(collectionR, k-lenL-1, recs+1)


#Test on wordlst
words = [word.strip() for word in open('wordlst.txt')]
if(len(words)%2 == 0):
	k=len(words)/2
else:
	k=math.ceil(len(words)/2.0)
print(string_selection(words, k, 0))


def maxminave(inFile):
	recs = [int(rec.strip()) for rec in open(inFile)]
	mx = max(recs)
	mn = min(recs)
	av = sum(recs)/len(recs)

	print(mn)
	print(mx)
	print(av)

maxminave('recursions.txt')


'''
Sample Output
-------------
LUNK
7
37
21
'''