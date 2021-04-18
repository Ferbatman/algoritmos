peso_saco = int(input("Informe aqui o valor do saco de ração em gramas: "))
racao_gato1 = int(input("Qual a quantidade de ração colocada para o primeiro gato? "))
racao_gato2 = int(input("Qual a quantidade de ração colocada para o segundo gato? "))

total_final = peso_saco - 5 * (racao_gato1 + racao_gato2)

print("Após 5 dias de ração sobrou {} gramas de ração no saco.".format(total_final))