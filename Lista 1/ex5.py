print("Vamos aumentar teu salário")

salario = float(input("Informe aqui teu salário: "))
percentual = float(input("Informe aqui qual a porcentagem de aumento do salario: "))
aumento = salario * percentual/100

novo_salario = salario + aumento

print("O salário a receber é de R$ {:.2f}".format(novo_salario))