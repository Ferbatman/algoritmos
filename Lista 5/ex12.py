"""Faça um programa que:
preencha um vetor com quinze elementos inteiros
verifique a existência de elementos iguais a 30, mostrando os índices/posições em que apareceram."""

vetor = []
indice = []

for i in range(5):
    vetor.append(int(input('Digite um número inteiro: ')))

for i in range(5):
    if vetor[i] == 30:
        indice.append(i)

if 30 in vetor:
    print(f'Os números 30 se encontram nos índices {indice}')
else:
    print('Não existe nenhum número 30 nessa lista')