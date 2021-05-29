"""Faça um programa que preencha um vetor com sete números inteiros. Calcule e mostre:
os números múltiplos de 2;
os números múltiplos de 3;
os números múltiplos de 2 e de 3."""

numeros = []
num2 = []
num3 = []
num = []

for i in range (7):
    numeros.append(int(input("Digite um número inteiro: ")))

for i in range (7):
    if numeros[i] % 2 == 0:
        num2.append(numeros[i])

for i in range (7):
    if numeros[i] % 3 == 0:
        num3.append(numeros[i])

for i in range (7):
    if numeros[i] % 2 == 0 and numeros[i] % 3 == 0:
        num.append(numeros[i])

print(f'Os números multiplos de 2 são {num2}')
print(f'Os números multiplos de 3 são {num3}')
print(f'Os números multiplos de 2 e 3 são {num}')