
def empty(L):
    return L == []

def head(L): # topo
    return L[0]

def tail(L):
    return L[1:]

def cons(x, L):
    return [x]+L

# LO -> Lista ordenada.
def insert(x, LO):
    if empty(LO):
        return [x]
    if x < head(LO):
        return cons(x, LO)
    else:
        return cons(head(LO), insert(x, tail(LO)))

# Insertion Sort (recursivo)
def isort(L):
    if empty(L):
        return []
    return insert(head(L), isort(tail(L)))

#######################
L = []
L = cons(2, L)
L = cons(7, L)
L = cons(1, L)
L = cons(8, L)
L = isort(L)
print(L)
