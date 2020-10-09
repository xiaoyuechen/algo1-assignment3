# This version is for Python 2.7.x
# Name 1: 
# Name 2: 

import random

# Random DNA string of length 2*n
def randstring(n):
    return "".join(random.choice(["AT","TA","CG", "GC"]) for i in range(0, n))

# Print the hash table
def output(t):
    for k in range(0, len(t)):
        s = str(k) + ": "
        if len(t[k]) <= 30:
            for i,e in enumerate(t[k]):
                if i != 0:
                    s = s + ","
                s = s + str(e)
        else:
            s = s + "(" + str(len(t[k])) + " elements)"

        print s

# Construct an empty hash table with n buckets
def ht(n):
    return map(lambda x: [], range(n))

# Hash function h1
def h1(e):
    return (37 * e) % 11

# Hash function h2
def h2(e):
    return (30 * e) % 8 

# Hash function h3
def h3(e):
    return (e*e) % 23

# Hash function h4 (defined on strings, as the sum of all character values)
def h4(e):
    return sum(map(ord, e)) % 19
