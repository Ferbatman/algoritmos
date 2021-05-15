# 6. Faça um programa que carregue um vetor com dez nomes e faça uma verificação se um determinado nome esta nesse vetor. Não use nenhuma função pronta da linguagem Python.

lista_nomes = []

for i in range(10):
    lista_nomes.append(input('Digite um nome: '))

nome = input('Digite um nome para procurar na lista: ')

if nome in lista_nomes:
    print(f'O nome {nome} consta na lista!')
else:
    print(f'O nome {nome} não consta na lista!')


