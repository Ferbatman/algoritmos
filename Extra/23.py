"""Faça um programa que:
leia um vetor com quinze posições para números inteiros.
depois da leitura, divida todos os seus elementos pelo maior valor do vetor.
Mostre o vetor após os cálculos.
não use nenhuma função pronta da linguagem Python"""


vetor = []
maior = 0

for i in range(15):
    vetor.append(int(input('Digite um número: ')))

for i in range(15):
    if vetor[i] > maior:
        maior = vetor[i]
print(f'O número com maior valor no vetor foi o {maior}')

for i in range(15):
    print(f'{vetor[i]} dividido por {maior} é', vetor[i] / maior)