# Aula 13/05 - Algoritmo do pow()

# Como se calcula x^a mod N de forma eficiente?
# Qual é o método do pow()? (Do C e Python)

# 2^0 mod 5 = 1 mod 5 = 1
# 2^31 mod 5? <-- Square-and-multiply

# 2^31 = 2^30 * 2  <-- square
# 2^30 = (2^15)^2  <-- multiply

# Se for ímpar, multiplica...
# Se for par, quebra na metade...
# (...)
# Caso base.
# Mais detalhado em: square-and-multiply.txt

def sam(x,a ,N): # square-and-multiply
    if zero(a):
        return 1
    if odd(a): # Suponha sam(x,a-1,N)
        return mult(x, sam(x, a-1, N), N)
    else:
        return sq(sam(x, a//2, N), N)

def zero(n): # é zero
    return n == 0

def remainder(a,b):
    return a%b

def even(n): # é par
    return remainder(n,2) == 0

def odd(n): # é ímpar
    return remainder(n,2) != 0

def mult(x, y, N):
    return remainder(x*y, N)

def sq(x, N):
    return mult(x, x, N)


# Ex: 4^16 mod 3 ?
print(sam(4, 16, 3))
