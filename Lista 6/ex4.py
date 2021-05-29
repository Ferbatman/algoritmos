'''Faça um programa para armazenar em uma matriz 5x2 preços. Encontre e apresente os ÍNDICES dos valores menores que 23 reais.'''

matriz = []

for l in range(5):
    vetor=[]
    for c in range(2):
        vetor.append(float(input(f'Insira o preço do item [{l}][{c}] ')))
    matriz.append(vetor)

print('-=' * 15)  
for l in range(5):
    for c in range(2):
        print(f'[{matriz[l][c]:^9.2f}]', end='\t')
    print()

print('-=' * 15, '\n')
for l in range(5):
    for c in range(2):
        if matriz[l][c] < 23:
            print(f'O produto no indice {[l]}{[c]} é menor que R$ 23,00')

