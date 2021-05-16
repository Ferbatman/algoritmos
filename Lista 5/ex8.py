# Criar um algoritmo que a partir de um vetor de 10 elementos inteiros, crie outros dois vetores que receberão os elementos positivos e negativos e ao final apresente-os. Não use nenhuma função pronta da linguagem Python.

numeros = []
positivo = []
negativo = []

for i in range(10):
    numeros.append(int(input("Digite um número inteiro positivo ou negativo: ")))
    if numeros[i] < 0:
        negativo.append(numeros[i])
    else:
        positivo.append(numeros[i])

print(f"Os números positivos foram {positivo}")
print(f"Os números negativos foram {negativo}")
