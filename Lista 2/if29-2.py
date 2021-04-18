import sys

salario_minimo = float(input('Coloque o salário mínimo: R$ '))
turno = input('Insira o turno:\n M - (Matutino)\n V - (Vespertino)\n N - (Noturno)\n').upper()
categoria = input('Insira a categoria:\n O - (Operário)\n G - (Gerente)\n').upper()
hrs_trab = float(input('Insira o número de horas trabalhadas: '))

# Checa se o turno é válido
if turno not in "MNV":
    print("Entre com um turno válido")
    sys.exit() # Encerra o programa aqui

# Checa se a categoria é válida
if categoria not in "OG":
    print("Entre com uma categoria válida")
    sys.exit()

if turno == "M":
    coeficiente = salario_minimo * 0.10
    salario_bruto = hrs_trab * coeficiente

elif turno == "V":
    coeficiente = salario_minimo * 0.15
    salario_bruto = hrs_trab * coeficiente

elif turno == "N":
    coeficiente = salario_minimo * 0.20
    salario_bruto = hrs_trab * coeficiente

if categoria == "O":
    if salario_bruto >= 300:
        imposto = salario_bruto * 0.05
    else:
        imposto = salario_bruto * 0.03

elif categoria == "G":
    if salario_bruto >= 300:
        imposto = salario_bruto * 0.06
    else:
        imposto = salario_bruto * 0.04

print(f'O valor do seu salário bruto é de R$ {salario_bruto:.2f}')
print(f'O imposto do seu salário é de R$ {imposto:.2f}')

if turno == "N" and hrs_trab > 80:
    gratificacao = 50
else:
    gratificacao = 30

print(f'Sua gratificação é de R$ {gratificacao:.2f}')

if categoria == "O" and coeficiente <= 25:
    auxilio = salario_bruto * (1/3)
else:
    auxilio = salario_bruto * (1/2)

print(f'Seu auxilio é de R$ {auxilio:.2f}')

salario_liquido = salario_bruto - imposto + gratificacao + auxilio

print(f'Seu salário liquido é de R$ {salario_liquido}')

if salario_liquido < 350:
    print('Mal remunerado!')
elif salario_liquido >= 350 and salario_liquido <= 600:
    print('Remuneração normal!')
elif salario_liquido > 600:
    print('Bem remunerado!')