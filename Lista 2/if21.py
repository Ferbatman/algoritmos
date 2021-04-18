salario_minimo = float(input('Insira seu salário mínimo: '))
hrs_trabalhadas = float(input('Insira suas horas trabalhadas: '))
dependentes = int(input('Insira quantos funcionáros dependentes: '))
hrs_extra = float(input('Insira suas horas extras: '))

valor_hr = 1/5 * salario_minimo
salario_mes = salario_minimo * valor_hr
valor_dependentes = dependentes * 32
valor_hr_extra = hrs_extra * (valor_hr + (valor_hr * 50/100))
salario_bruto = salario_mes + valor_dependentes + valor_hr_extra

if salario_bruto < 200:
    imposto = 0
elif salario_bruto >= 200 and salario_bruto <= 500:
    imposto = salario_bruto * (10/100)
else:
    imposto = salario_bruto * (20/100)

salario_liquido = salario_bruto - imposto

if salario_liquido <= 350:
    gratificacao = 100
else:
    gratificacao = 50

receber = salario_liquido + gratificacao

print(f'O funcionário tem a receber R$ {receber:.2f}')
