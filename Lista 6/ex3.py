"""Faça um programa que carregue uma matriz 3 x 2, que representa preços de produtos, crie OUTRA matriz que armazene todos os preços com 7% de aumento."""

matriz = []
matriz_nova= []

for lin in range(3):

    vetor_linha = []
    vetor_linha_nova = []

    for col in range(2): 

        vetor_linha.append(float(input(f'Digite o preço [ {str(lin)} ][ {str(col)} ] R$ ')))

        vetor_linha_nova.append(float(vetor_linha[col] + vetor_linha[col] * 0.07))
    
    matriz.append(vetor_linha)
    matriz_nova.append(vetor_linha_nova)

print('\nMatriz original')
for lin in range(3):
    for col in range(2):
        print(f'{matriz[lin][col]:.2f}', end='\t')
    print()

print('\nMatriz com aumento de 7%')
for lin in range(3):
    for col in range(2):
        print(f'{matriz_nova[lin][col]:.2f}', end='\t')
    print()


