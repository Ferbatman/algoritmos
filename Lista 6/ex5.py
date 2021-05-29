'''Faça um programa que leia números inteiros m e n e os elementos de uma matriz A de números inteiros de dimensão m x n e conte o número de elementos que são iguais a zero.'''

m = int(input("Digite um número inteiro: "))
n = int(input("Digite um número inteiro: "))
matriz = []
cont = 0

for l in range(m):
    vetor = []
    for c in range(n):
        vetor.append(int(input(f'Digite um valor inteiro para posição {[l]}{[c]}: ')))
    matriz.append(vetor)

for l in range(m):
    for c in range(n):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] == 0:
            cont += 1
    print()

print(f'\nExistem {cont} elementos iguais a zero nessa matriz!')