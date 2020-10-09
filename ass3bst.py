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


def deleteinordersuccessor(t):
    key, left, right = t
    if (left == None) and (right == None):
        return (key, None)
    successor_value, tleft = deleteinordersuccessor(left)
    return (successor_value, (key, tleft, right))


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
            successor_value, nt = deleteinordersuccessor(t)
            return (successor_value, nt[1], nt[2])
    elif x < key:
        return (key, delete(left, x), right)
    return (key, left, delete(right, x))


if __name__ == "__main__":
    print("====== inorder walk test")
    inorderwalk(treefromlist([10, 3, 5, 1]))
    print()

    print("====== delete test 1")
    t4 = treefromlist([2, 6, 7, 4, 1])
    print("original tree")
    print("remove 6")
    print(t4)
    t4 = delete(t4, 6)
    print("result tree")
    print(t4)

    print("====== delete test 2")
    print("original tree")
    print("remove 1")
    t5 = insert(emptytree(), 1)
    t5 = delete(t5, 1)
    print("result tree")
    print(t5)
