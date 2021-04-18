print(" Menu de opções: \n 1.Somar dois numeros. \n 2.Raiz quadrada de um número.")
a = int(input("Selecione uma das opções anteriores: "))

if a == 1:
    n1 = float(input("Insira um número: "))
    n2 = float(input("Insira um número: "))
    n3 = n1 + n2
    print(f"A soma do número {n1} mais {n2} é igual {n3}")

if a == 2:
    from math import sqrt
    n1 = float(input("Insira um número: "))
    raiz = sqrt(n1)
    print(f"A raiz quadrada de {n1} é {raiz}")