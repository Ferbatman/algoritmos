"""2. Faça um programa que carregue uma matriz 2 x 2, que representa o salário de 4 funcionários, calcule e mostre a soma total de todos os elementos que será o montante pago pela empresa a esses funcionários."""

# soma = soma + salario[lin][col]

salario = []

for lin in range(2):

    vetor_linha_com_2_colunas = []

    for col in range(2): 

        vetor_linha_com_2_colunas.append(int(input('Digite o salário ['+ str(lin) + '][' + str(col) + '] R$ ')))

    salario.append(vetor_linha_com_2_colunas)

soma = 0

for lin in range(len(salario)): #len(matriz) mostra a qtde de linhas)

    for col in range(len(salario[0])): #len(matriz[0] mostra a qtde de colunas)

        soma = soma + salario[lin][col]

        print('R$ ', str(salario[lin][col]), end='\t')

    print()

print('O montante de salários pagos pela empresa é R$',soma)
