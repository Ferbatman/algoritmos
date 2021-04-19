i = 0
soma = 0
while i < 5:
    preco = (float(input("Coloque o preço de um produto: ")))
    soma += preco
    i += 1

media = soma / i
print(f"A média dos 5 produtos são de R$ {media:.2f}")