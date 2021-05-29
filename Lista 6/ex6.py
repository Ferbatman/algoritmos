'''Faça um programa que carregue: *um vetor com oito posições com os nomes das lojas; * um outro vetor com quatro posições com os nomes dos produtos; * uma matriz com os preços de todos os produtos em cada loja. O programa deve mostrar todas as relações (nome do produto – nome da loja) nas quais o preço não ultrapasse R$ 120,00. Escolha qual é o tipo da função que quer.'''

loja = [str(input('Digite o nome da loja: ')) for i in range(3)]
produto = [str(input('Digite o nome do produto: ')) for i in range(2)]
matriz = []

for l in range(3):
    preco = []
    for c in range(2):
        preco.append(float(input(f'Digite o preço do {produto[c]} na {loja[l]}: ')))
    matriz.append(preco)

for i in range(2):
    print(f'[{produto[i]:^7}]', end=' ')

print('\n')

for l in range(3):
    for c in range(2):
        print(f'[{matriz[l][c]:^7.2f}]', end=' ')
    print()

for l in range(3):
    for c in range(2):
        if matriz[l][c] <= 120:
            print(f'O produto {produto[c]} na loja {loja[l]} custa R$ {matriz[l][c]:.2f}')
        

