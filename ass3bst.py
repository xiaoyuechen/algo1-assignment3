# This version is for both Python 2.7.x and 3.x.x
# Name 1:
# Name 2:

# Create empty tree
def emptytree():
    return None

# Insert x into tree t


def insert(t, x):
    if t == None:
        return (x, None, None)
    else:
        key, left, right = t
        if x == key:
            return (key, left, right)
        elif x < key:
            return (key, insert(left, x), right)
        else:
            return (key, left, insert(right, x))

# Create tree by inserting each element in l into an initially empty tree


def treefromlist(l):
    t = emptytree()
    for x in range(0, (len(l))):
        t = insert(t, l[x])
    return t


def inorderwalk(t):
    if t == None:
        return
    key, left, right = t
    inorderwalk(left)
    print(key, end=" ")
    inorderwalk(right)


def minimum(t):
    _, left, _ = t
    if left == None:
        return t
    return minimum(left)


def successorinchildren(node):
    _, _, right = node
    return minimum(right)


def delete(t, x):
    if t == None:
        return None
    key, left, right = t
    if key == x:
        if (left == None) and (right == None):
            return None
        elif (left != None) and (right == None):
            return left
        elif (left == None) and (right != None):
            return right
        elif (left != None) and (right != None):
            skey, _, _ = successorinchildren(t)
            return (skey, left, delete(right, skey))
    elif x < key:
        return (key, delete(left, x), right)
    return (key, left, delete(right, x))


def inorderwalktest(t, idx):
    print("================== in-order walk test %d ==================" % idx)
    print("tree %s" % str(t))
    inorderwalk(t)
    print()


def deletetest(t, x, idx):
    print("================== delete test %d ==================" % idx)
    print("before %s" % str(t))
    print("delete %d" % x)
    r = delete(t, x)
    print("after %s" % str(r))


if __name__ == "__main__":
    t1 = treefromlist([10, 3, 5, 1])
    inorderwalktest(t1, 1)

    t2 = treefromlist([6, 2, 7, 0, 9, 8, 66, 3, 5, 1])
    inorderwalktest(t2, 2)

    t1 = treefromlist([2, 6, 7, 4, 1])
    deletetest(t1, 6, 1)

    t2 = insert(emptytree(), 1)
    deletetest(t2, 1, 2)

    t3 = treefromlist([1, 5, 3, 7, 0, 9])
    deletetest(t3, 2, 3)

    t4 = treefromlist([1, 5, 3, 7, 0, 9])
    deletetest(t4, 5, 4)

    t5 = treefromlist([7, 4, 5, 6, 2, 0, 9, 8])
    deletetest(t5, 4, 5)
