"""16. Faça um programa que:
preencha dois vetores com de dez numeros cada
preencha um terceiro vetor com os números dos dois vetores anteriores ordenados em ordem crescente"""

num1 = []
num2 = []

for i in range(10):
    num1.append(float(input('Digite um número para lista 1: ')))

for i in range(10):
    num2.append(float(input('Digite um número para lista 2: ')))

num3 = num1 + num2
num3.sort()

print(f'Vetor 1: {num1}')
print(f'Vetor 2: {num2}')
print(f'A junção de ambos vetores em ordem crescente é: {num3}')
