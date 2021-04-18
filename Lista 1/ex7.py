salario = float(input("Informe aqui o salário base do funcionario: "))

perImposto = float(input("Informe aqui a porcentagem do imposto: "))

imposto = salario * perImposto / 100

salario_a_receber = salario + 50 - imposto

print("O salário a receber é de R$ {:.2f}".format(salario_a_receber))