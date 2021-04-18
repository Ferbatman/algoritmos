preco_fabrica = float(input("Informe aqui o valor de fábrica do carro: "))
percentual_lucro_distribuido = float(input("Informe aqui a porcentagem de lucro do distribuidor: "))
percentual_imposto = float(input("Informe aqui a porcentagem de imposto do carro: "))

lucro_distribuidor = preco_fabrica * percentual_lucro_distribuido / 100
valor_imposto = preco_fabrica * percentual_imposto / 100
preco_final = preco_fabrica + lucro_distribuidor + valor_imposto

print("O valor de lucro do distribuidor é de R$ {:.2f}".format(lucro_distribuidor))
print("O valor dos impostos são de R$ {:.2f}".format(valor_imposto))
print("O valor final do veículo é de R$ {:.2f}".format(preco_final))