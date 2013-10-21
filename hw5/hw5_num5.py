


#hw5_num5.py
#Austin Longo
#10/22/13

#! /usr/bin/python
import sys
import random
import math
import string
import bisect


#//////////////////////////////////////////////////////////////////////////////
#word_chain takes a collection of words, converts them to alphagrams and outputs
#one of the longest word chains
def word_chain(collection):
	#map the alphagramatize function onto each word in collection
	new_list = map(alphagramatize, collection)
	
	#remove duplicates by converting to a set
	new_list = set(new_list)

	#convert back to a list... cause I like lists
	new_list = list(new_list)
	
	#sort the set
	new_list.sort()

	#create new empty graph
	g = Graph()

	#add all words to graph
	for word in new_list:
		g.addVertex(word)

	#fill graph with valid word chains
	for word in g.getVertices():
		for c in string.ascii_lowercase:
			new_word = alphagramatize(word+c)
			if(binary_search(new_list, new_word) != -1):
				g.addEdge(word, new_word)
				print(new_word)
    
    print(g.getVertices())
    print(g.printEdges())
    print(g.getEdges())
	
    g.dfs
#//////////////////////////////////////////////////////////////////////////////


#Helper Functions//////////////////////////////////////////////////////////////
#alphagramatize converts the input collection, or word, to its alphagram
def alphagramatize(word): 
	word = word.upper()
	return ''.join(sorted(c for c in word if c >= 'A' and c <= 'Z'))

#------------------------------------------------------------------------------
#Binary search function implemented with the bisect module
def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect.bisect_left(a,x,lo,hi)   # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end
#//////////////////////////////////////////////////////////////////////////////



#Graph Data Structure//////////////////////////////////////////////////////////
class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.visited = False
        self.component = -1
        self.startTime = -1
        self.finishTime = -1

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def __iter__(self):
    	return(iter(self.connectedTo.values()))

    def getId(self):
        return self.id

#Graph-------------------------------------------------------------------------
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.componentCntr = 0
        self.time = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def printEdges(self):
    	for v in self.__iter__():
    		print(v.__str__())

    def getEdges(self):
        return iter(v.__iter__())

    def dfs(self):
    	for src_word in self.getVertex():
 			if(v.visited == False):
 				explore(self, v)
 			self.componentCntr += 1

	def explore(self, v):
   		self.visit(v)
   		self.preVisit(v)

   		for v in v.__iter__():
   			print("blarg")
   		
   		self.postVisit(v)

    def visit(self, v):
    	v.visited = True

    def preVisit(self, v):
    	v.startTime = self.time
    	self.time += 1

    def postVisit(self, v):
    	v.stopTime = self.time
    	self.time += 1
#//////////////////////////////////////////////////////////////////////////////			


#------------------------------------------------------------------------------
#TESTS/RUNS
#------------------------------------------------------------------------------
#Test on readable amount of words (uncomment and comment other one)
words = ['cat', 'cat', 'catz', 'tac', 'cats', 'dog', 'dogs', 'godes', 'bird']

#words = [word.strip() for word in open('wordlst.txt')]
word_chain(words)