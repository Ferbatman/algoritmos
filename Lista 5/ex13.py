"""Faça um programa que preencha um vetor com dez números reais
Calcule e mostre:
a quantidade de números negativos
a soma dos números positivos desse vetor
não use nenhuma função pronta da linguagem Python"""

vetor = []
negativo = soma = 0

for i in range(5):
    vetor.append(float(input('Digite um número: ')))

for i in range(5):
    if vetor[i] < 0 :
        negativo += 1
    else:
        soma += vetor[i]

print(f'A quantidade de números negativos é {negativo}')
print(f'A soma de todos números positivos é {soma}')


