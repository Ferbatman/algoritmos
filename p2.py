salario = float(input('Informe o salário de um funcionário: '))

if salario <= 1100:
    inss = salario * 0.075
elif salario > 1100 and salario <= 2203.48:
    inss = salario * 0.09
elif salario > 2203.48 and salario <= 3305.22:
    inss = salario * 0.12
elif salario > 3305.22 and salario <= 6433.57:
    inss = salario * 0.14
else:
    inss = 751.97

salario_liquido = salario - inss

print(f'Com esse valor de salário o desconto do INSS é de R$ {inss:.2f} e o valor do salário líquido R$ {salario_liquido:.2f}')    

