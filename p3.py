y = x = 0

for i in range (1,11):
    salario = float(input('Informe o salário: '))

    if salario > 2000:
        x += 1
        y += salario        

media = y / x

print(f'A média entre funcionários com salário acima de R$ 2000, é de R$ {media:.2f}')
