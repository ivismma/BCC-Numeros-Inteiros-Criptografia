# Aula 13/05/2024
# Àrvores binárias de busca
# Binary Search Trees

# Definição B.S.T:
# [] ou...
# Tree(L, x, R)

# Para todo x pertencente a {qualquer conjunto}, e L e R sendo BSTs (!!!)

def empty(L):
    return L == []

def Tree(L, x, R):
    return L,x,R

# Esquerda:
def left(T):
    return T[0]
# Raiz:
def root(T):
    return T[1]
# Direita:
def right(T):
    return T[2]

def sort(L):
    if empty(L):
        return L
    return insertT(head(L), sort(tail(L))
# Inserção
def insertT(x, T):  # Indução estrutural
    if empty(T)
        return Tree([],x,[])
    else:
        if x < sort(T):
            return Tree(insertT(x, left(T)), root(T), right(T))
        else:
            return Tree(left(T), root(T), insertT(x, right(T)))
