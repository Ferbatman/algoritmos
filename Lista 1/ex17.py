salario = float(input("Informe o valor do teu salário: "))
valor_cheque1 = float(input("Informe o valor do primeiro cheque: "))
valor_cheque2 = float(input("Informe o valor do segundo cheque: "))

imposto_cheque1 = valor_cheque1 * 0.38 / 100
saque1 = valor_cheque1 + imposto_cheque1
imposto_cheque2 = valor_cheque2 * 0.38 / 100
saque2 = valor_cheque2 + imposto_cheque2
saldo = salario - saque1 - saque2

print("O seu saldo disponível é de R$ {:.2f}".format(saldo))