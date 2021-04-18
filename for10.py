soma = 0
for i in range(1, 6):
    idade = (int(input("Coloque uma idade: ")))
    soma += idade

media = soma / i
print(f"A média das idades é de {media:.0f} anos!")