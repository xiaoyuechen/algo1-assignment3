# This version is for Python 3.x.x
# Name 1: Dmitrii Markov
# Name 2: Mattias Kynde Hämberg
# Name 3: Xiaoyue Chen

import random


# Random DNA string of length 2*n
def randstring(n):
    return "".join(random.choice(["AT", "TA", "CG", "GC"]) for i in range(0, n))


# Print the hash table
def output(t):
    for k in range(0, len(t)):
        s = str(k) + ": "
        if len(t[k]) <= 30:
            for i, e in enumerate(t[k]):
                if i != 0:
                    s = s + ","
                s = s + str(e)
        else:
            s = s + "(" + str(len(t[k])) + " elements)"

        print(s)


# Construct an empty hash table with n buckets
def ht(n):
    return list(map(lambda x: [], range(n)))


# Hash function h1
def h1(e):
    return (37 * e) % 11


# Hash function h2
def h2(e):
    return (30 * e) % 8


# Hash function h3
def h3(e):
    return (e * e) % 23


# Hash function h4 (defined on strings, as the sum of all character values)
def h4(e):
    return sum(map(ord, e)) % 19


def insert(t, h, e):
    index = h(e) % len(t)
    t[index].append(e)


def search(t, h, e):
    index = h(e) % len(t)
    for x in t[index]:
        if x == e:
            return True
    return False


def delete(t, h, e):
    index = h(e) % len(t)
    for i in range(len(t[index])):
        if t[index][i] == e:
            t[index].pop(i)
            return


def test1():
    t = ht(11)
    for i in range(1000):
        r = random.randint(0, 10000)
        insert(t, h1, r)
    output(t)


def test2():
    t = ht(8)
    for i in range(1000):
        r = random.randint(0, 1000)
        insert(t, h2, r)
    output(t)


def test3():
    t = ht(23)
    for i in range(1000):
        r = random.randint(10000000, 100000000000)
        insert(t, h3, r)
    output(t)


def test4():
    t = ht(11)
    keys = [1, 12, 23, 34, 45, 56, 67, 78, 89, 100, 111]
    for k in keys:
        insert(t, h1, k)
    output(t)


def testdna():
    t = ht(19)
    for i in range(1000):
        rdna = randstring(10)
        insert(t, h4, rdna)
    output(t)
