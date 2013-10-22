


#hw5_num5.py
#Austin Longo
#10/22/13

#! /usr/bin/python
import sys
import random
import math
import string
import bisect
import collections
import networkx as nx

#//////////////////////////////////////////////////////////////////////////////
#word_chain takes a collection of words, converts them to alphagrams and outputs
#one of the longest word chains
def word_chain(collection):
    #map the alphagramatize function onto each word in collection
    new_list = map(alphagramatize, collection)

    #print(new_list)
    #remove duplicates by converting to a set
    new_list = set(new_list)

    #convert back to a list... cause I like lists
    new_list = list(new_list)

    #sort the list
    new_list.sort()

    #create new empty graph
    g = nx.DiGraph()

    #add all words to graph
    for word in new_list:
        g.add_node(word)

    #fill graph with valid word chains
    for word in g.nodes():
        for c in string.ascii_lowercase:
            new_word = alphagramatize(word+c)
            if(binary_search(new_list, new_word) != -1):
                g.add_edge(word, new_word)

    print longest_path(g)

    print(g.nodes())
    print(g.edges())

#//////////////////////////////////////////////////////////////////////////////

def longest_path(G):
    dist = {} # stores [node, distance] pair
    for node in nx.topological_sort(G):
        pairs = [[dist[v][0]+1,v] for v in G.pred[node]] # incoming pairs
        if pairs:
            dist[node] = max(pairs)
        else:
            dist[node] = (0, node)
    node, max_dist  = max(dist.items())
    path = [node]
    while node in dist:
        node, length = dist[node]
        path.append(node)
    return list(reversed(path))


#Helper Functions//////////////////////////////////////////////////////////////
#alphagramatize converts the input word to its alphagram
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




#------------------------------------------------------------------------------
#TESTS/RUNS
#------------------------------------------------------------------------------
#Test on readable amount of words (uncomment and comment other one)
words = ['a', 'aa', 'catz', 'cat', 'cat', 'tac', 'cats', 'dog', 'dogs', 'godz', 'godes', 'bird']

#words = [word.strip() for word in open('wordlst.txt')]
word_chain(words)
