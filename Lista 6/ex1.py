matriz = []

for lin in range(2):

    linha = []

    for col in range(3): 

        linha.append(int(input('Digite o valor de ['+ str(lin) + '][' + str(col) + ']: ')))

    matriz.append(linha)



for lin in range(len(matriz)): #len(matriz) mostra a qtde de linhas)

    for col in range(len(matriz[0])): #len(matriz[0] mostra a qtde de colunas)

        print(matriz[lin][col],' Linha:'+ str(lin) + ' Coluna:'+ str(col))