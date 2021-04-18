qtde_horas_trabalhadas = float(input("Insira aqui o total de horas trabalhadas: "))
salario_minimo = float(input("Coloque o valor do salário mínimo: "))

valor_hora_trabalhada = salario_minimo / 2
valor_salario_bruto = valor_hora_trabalhada * qtde_horas_trabalhadas
imposto = valor_salario_bruto * 3 / 100
Valor_salario_liquido =  valor_salario_bruto - imposto

print("O salário que você tem a receber é de R$ {:.2f}".format(Valor_salario_liquido))