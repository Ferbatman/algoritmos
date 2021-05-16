# 9. Criar um algoritmo que leia dados para um vetor de 10 elementos inteiros, imprimir o maior, o menor, o percentual de números pares e a média dos elementos do vetor. Obs.: percentual = quantidade contada * 100 / quantidade total. Não use nenhuma função pronta da linguagem Python.

numeros = []
pares = []
cont = 0
soma_num = 0

for i in range(10):
    numeros.append(int(input("Digite um número inteiro: ")))

# achado o maior e o menor número
for i in range(10):
    if i == 0:
        menor = numeros[i]
        maior = numeros[i]
    if numeros[i] > maior:
        maior = numeros[i]
    elif numeros[i] < menor:
        menor = numeros[i]

# percentual de números pares
for i in range(10):
    if numeros[i] % 2 == 0:
        cont += 1
        pares.append(numeros[i])

percent = (cont * 100) / 10

# média dos números
for i in range(10):
    soma_num += numeros[i]

media = soma_num / len(numeros)


print(numeros)
print(f'O maior número foi {maior} e o menor número foi {menor}')
print(f"O percentual dos números pares foi de {percent} %")
print(f"A média dos elementos da lista foi de {media}")
