""" Faça um programa que:
carregue dois vetores com 10 números cada
faça a multiplicação dos números na mesma posição
o resultado deverá ser adicionada em um terceiro vetor
não use nenhuma função pronta da linguagem Python"""

lista1 = [float(input('Digite um número para lista 1: ')) for i in range(10)]
lista2 = [float(input('Digite um número para lista 2: ')) for i in range(10)]
lista3 = [lista1[i] * lista2[i] for i in range(10) ]

print(f'Vetor 1: {lista1}')
print(f'Vetor 2: {lista2}')
print(f"A multiplicação dos números na mesma posição é: {lista3}")