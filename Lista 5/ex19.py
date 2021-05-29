'''19. Faça um programa que:
insira dez números inteiros em um vetor
crie um segundo vetor, substituindo os números multiplos de 3 por "999""
exiba os dois vetores
não use nenhuma função pronta da linguagem Python'''

vetor1 = []
vetor2 = []

for i in range(5):
    vetor1.append(int(input('Digite um número inteiro: ')))
    if vetor1[i] % 3 == 0:
        vetor2.append(vetor1[i])
        vetor2[i] = 999
    else:
        vetor2.append(vetor1[i])

print(vetor1)
print(vetor2)
