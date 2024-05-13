# Aula 13/05/2024
# Quero iD. Bézout
# b = xa + yb

# Qual o caso base do Alg Estendido?

def divides(a,b):
    return a%b == 0

def xmdc(a,b): # m, x, y
    if divides(a,b):
        return b, 0, 1
    # xmdc(b, r)

    q, r = divmod(a,b)
    m, x, y = xmdc(b,r)
    return m, y, x-q*y


def bezout(a, b):
    m, x, y = xmdc(a,b)
    return f"{m} = {x}*{a} + {y}*{b}"


# Ex da lista 1: 37x+23y = 1.
print(bezout(37,23))
