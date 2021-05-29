# 5. Faça um programa que carregue um vetor de oito elementos numéricos inteiros, calcule e mostre os números pares e suas respectivas índices/posições. Não use nenhuma função pronta da linguagem Python.

num = []

for i in range(8):
    num.append(int(input('Digite um numero: ')))

for i in range(8):
    if num[i] % 2 == 0:
        print(f'O numero {num[i]} é par, e ele se encontra no indice {i}')




