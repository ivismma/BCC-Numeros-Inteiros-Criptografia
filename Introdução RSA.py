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

    print("Gerando p e q")
    p = randprime(2**1025, 2**1026)
    q = randprime(2**1025, 2**1026)

    print("Calculando n, Φ(n) e expoente...")
    n = p*q
    phi_n = (p-1)*(q-1)
    e = 65537

    # Inverso multiplicativo modular (Alg. de Euclides):
    print("Descobrindo a chave privada...")
    d = inverso(e, phi_n)

    print("Obs: A mensagem (m) a ser encriptada deverá respeitar o seguinte intervalo: 0 <= m <= n")
    m = int(input("\nDigite um número inteiro a ser encriptado: "))
    print("Encriptando...")
    c = (m**e) % n
    print("Encriptado.")

    ### DECRIPTAÇÃO:
    
    decrypt = pow(c,d,n)
    # square-and-multiply

    print("Desencriptando...\nMensagem:", decrypt)

    return 0


main()

# Observações: Nesse programa, para fins de estudos, criptografei e descriptografei uma
# mensagem RSA, com valores *inteiros* (nome da disciplina -> Numeros Inteiros Criptografia)
