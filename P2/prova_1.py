#Em Python crie um programa que leia uma matriz e verifique/apresente se ela "é simétrica" ou "não é simétrica". Uma matriz é considerada simétrica quando a quantidade de linhas é igual a quantidade de colunas.

linhas = int(input("Digite um número de linhas: "))
colunas = int(input("Digite um número de colunas: "))
matriz = []

for l in range(linhas):
    vetor = []
    for c in range(colunas):
        vetor.append(int(input(f'Digite um número para a posição [{l}] [{c}]: ')))
    matriz.append(vetor)

for l in range(linhas):
    for c in range(colunas):
        print(f'|{matriz[l][c]:^5}|', end=' ')
    print()

if linhas == colunas:
     print('\nEssa matriz é simétrica!!')
else:
     print('\nEssa matriz não é simétrica!!')

