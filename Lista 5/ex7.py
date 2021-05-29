# 7. Faça um algoritmo que calcule e apresente a média de alturas superior a 1,80 de 10 alunos. Informe também quantos e quais (índice/posição) são os alunos. Não use nenhuma função pronta da linguagem Python.
import sys

altura = []
altura_m = 0
cont = 0
indice = []

for i in range(10):
    altura.append(float(input("Digite a altura do aluno: ")))
    
for i in range(10):    
    if altura[i] > 1.8:
        altura_m += altura[i]
        cont += 1
        indice.append(i)
        
if cont == 0:  # caso nenhum aluno tenha altura não vai dar erro
    print('Não tem nenhum aluno com altura superior a 1.80')
    sys.exit()

media = altura_m / cont
print(f'A media de altura dos alunos superiores a 1.80 é de {media:.2f}')
print(f'Existem {cont} alunos com altura superior a 1.80, e eles se encontram no índice {indice}')
