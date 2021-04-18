salario = float(input("Informe seu salário: "))

if salario < 500:
    bonus = salario * 0.05
elif salario >= 500 and salario <= 1200:
    bonus = salario * 0.12
else:
    bonus = 0

if salario <= 600:
    auxilio = 150
else:
    auxilio = 100

novo_salario = salario + bonus + auxilio
print(f"Seu novo salário é de R$ {novo_salario:.2f}")