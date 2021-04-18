salario_base = float(input('Insira seu salário base: R$ '))
tempo = float(input('Insira seu tempo de serviço em anos: '))

if salario_base < 200:
    imposto = 0
elif salario_base >= 200 and salario_base <= 450:
    imposto = salario_base * 0.03
elif salario_base > 450 and salario_base < 700:
    imposto = salario_base * 0.08
else:
    imposto = salario_base * 0.12
print(f'O imposto é de R$ {imposto:.2f}')

if salario_base > 500:
    if tempo <= 3:
        gratificação = 20
    else:
        gratificação = 30
else:
    if tempo <= 3:
        gratificação = 23
    elif tempo > 3 and tempo < 6:
        gratificação = 35
    else:
        gratificação = 33
print(f'Sua gratificação é de R$ {gratificação:.2f}')

salario_liquido = salario_base - imposto + gratificação
print(f'Seu salário liquido é de R$ {salario_liquido:.2f}')

if salario_liquido <= 350:
    print('Classificação A')
elif salario_liquido > 350 and salario_liquido < 600:
    print('Classificação B')
else:
    print('Classificação C')
