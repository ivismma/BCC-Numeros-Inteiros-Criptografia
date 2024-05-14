# Aula 13/05/2024
# Àrvores binárias de busca
# Binary Search Trees

# Definição B.S.T:
# [] ou...
# Tree(L, x, R)

# Para todo x pertencente a {qualquer conjunto}, e L e R sendo BSTs (!!!)

def Tree(L, x, R):
    return L,x,R

def empty(L):
    return L == []

# Esquerda:
def left(T):
    return T[0]
# Raiz:
def root(T):
    return T[1]
# Direita:
def right(T):
    return T[2]

# Inserção na árvore
def insertT(x, T):  # Indução estrutural
    if empty(T):
        return Tree([],x,[])
    else:
        if x < root(T):
            return Tree(insertT(x, left(T)), root(T), right(T))
        else:
            return Tree(left(T), root(T), insertT(x, right(T)))

T = []
T = insertT(6, T)
T = insertT(9, T)
T = insertT(3, T)
print(T)
