contador = y = x = 0

while contador <= 10:
    salario = float(input('Informe o salário: '))

    if salario > 2000:
        x += 1
        y += salario

    contador += 1        

media = y / x

print(f'A média entre funcionários com salário acima de R$ 2000, é de R$ {media:.2f}')
