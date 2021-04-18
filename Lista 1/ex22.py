valor_salario = float(input("Coloque o valor salário mínimo: "))
qtde_quilowatt = float(input("Informe a quantidade de quilowatts consumido: "))

valor_quilowatt = valor_salario / 5
valor_em_reais = valor_quilowatt * qtde_quilowatt
valor_descontado = valor_em_reais * 15 / 100
valor_com_desconto =  valor_em_reais - valor_descontado

print("O valor de cada quilowatt é de {:.2f} reais".format(valor_quilowatt))
print("O valor total a ser pago é de R$ {:.2f}".format(valor_em_reais)) 
print("O valor total com desconto de 15% é de R$ {:.2f}".format(valor_com_desconto))