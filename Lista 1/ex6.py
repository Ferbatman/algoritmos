salario = float(input("Informe aqui o salário base do funcionario: "))

gratificacao = salario * 5 / 100
imposto = salario * 7 / 100
salario_a_receber = salario + gratificacao - imposto

print("O salário a receber é de R$ {:.2f}".format(salario_a_receber))
