"""Faça um programa que:
leia dois vetores (A e B) com cinco posições para números inteiros.
o programa deve, então, subtrair o primeiro elemento de A do último de B, armazenando o resultado num terceiro vetor, subtrair o segundo elemento de A do penúltimo de B, armazenando o resultado num terceiro vetor e assim por diante.
ao final, mostre o resultado do terceiro vetor
não use nenhuma função pronta da linguagem Python"""

vetor_A = []
vetor_B = []
vetor_C= []


for i in range(5):
    vetor_A.append(int(input('Digite um número inteiro: ')))

for i in range(5):
    vetor_B.append(int(input('Digite um número inteiro: ')))

inverso = vetor_B[::-1]

for i in range(5):
    vetor_C.append(inverso[i] - vetor_A[i])

print(vetor_C)
