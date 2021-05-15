#Faça um programa que carregue um vetor com a média de dez alunos, calcule e mostre a MÉDIA DA SALA e quantos alunos estão acima e abaixo da média da sala.

vet_media = []
soma_media = 0
alunos_cima = 0
alunos_baixo = 0

for i in range(10):
    vet_media.append(float(input(f'Insira a média do {i+1}º aluno: ')))
    soma_media = soma_media + vet_media[i]

media = soma_media / len(vet_media)

for i in range(10):
    if vet_media[i] >= media:
        alunos_cima += 1
    else:
        alunos_baixo += 1


print(f'A média de nota da sala com {i+1} alunos, é de {media}')
print(f'A quantidade de alunos acima da média é de {alunos_cima} alunos, e a quantidade de alunos abaixo da média é de {alunos_baixo} alunos')