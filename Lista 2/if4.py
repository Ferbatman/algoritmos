n = int(input("Digite um número inteiro: "))

if n % 2 == 0:
    print("Esse número é par")
else:
    print("Esse número é ímpar")

if n > 0:
    print("Esse número é positivo")
elif n == 0:
    print("Esse número é nulo")
else:
    print("Esse número é negativo")