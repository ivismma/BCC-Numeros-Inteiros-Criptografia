# Introdução RSA - Teste RSA

# 1. Sorteie dois primos p, q grandes de tamanhos similares. (Por exemplo, sorteie
# dois primos de aproximadamente 1024 bits cada um.) 
# Compute o produto n = pq.

# 2. Compute phi(n) = phi(p)phi(q) = (p − 1)(q − 1).

# 3. Sorteie um expoente e até que e satisfaça 2 < e < phi(n) e mdc(e, phi(n)) = 1.

# 4. Publique sua chave pública (n, e). (Por exemplo, publique em sua homepage.)

# 5. Usando e e phi(n), compute d tal que d*e ≡ 1 mod phi(n). O número d é sua chave
# privada guarde-a em segredo. (Por razões didáticas, destrua p, q e phi(n) ).

#####################################################################################

from sympy import randprime

def algoritmoEuclides(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        mdc, x, y = algoritmoEuclides(b % a, a)
        return (mdc, y - (b // a) * x, x)

def inverso(e, phi_n):
    mdc, x, y = algoritmoEuclides(e, phi_n)
    if mdc != 1:
        print("O inverso multiplicativo não existe")
        exit()
    else:
        return x % phi_n

def main():

    p = randprime(2**1025, 2**1026)
    q = randprime(2**1025, 2**1026)

    # n = p*q
    phi_n = (p-1)*(q-1)
    e = 65537

    # Inverso multiplicativo modular (Alg. de Euclides):
    d = inverso(e, phi_n)

    if (d*e)%phi_n == 1:
        print("A chave privada está correta (Descriptografa).")
    else:
        print("A chave privada está incorreta.")

    return 0


main()