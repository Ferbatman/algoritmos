"""Faça um programa que:
leia um vetor de 10 números inteiros
exiba na tela os números positivos e seus respectivos índices.
não use nenhuma função pronta da linguagem Python"""

lista = []

for i in range(10):
    lista.append(int(input("Digite um número inteiro: ")))

for i in range(10):
    if lista[i] > 0:
        print(f'O numero {lista[i]} é positivo e ele se encontra na posição {i}')