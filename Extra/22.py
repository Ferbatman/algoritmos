"""Faça um programa que:
preencha um vetor de cinco números e mostre a saída a seguir:
imprima a seguinte saída: n1 + n2 + n3 + n4 + n5 = soma_dos_numeros, exemplo 8 + 2 + 1 + 3 + 0 = 14
não use nenhuma função pronta da linguagem Python"""

lista = []

for i in range(5):
    lista.append(int(input('Digite um número: ')))

soma = lista[0] + lista[1] + lista[2] + lista[3] + lista[4]

print(f'{lista[0]} + {lista[1]} + {lista[2]} + {lista[3]} + {lista[4]} = {soma}')
