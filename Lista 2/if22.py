preco_atual = float(input('Qual o preço do produto? '))
venda_media = int(input('Qual a venda média desse produto mensalmente? '))

if venda_media < 500 or preco_atual < 30:
    novo_preco = preco_atual + ((10/100) * preco_atual)
elif venda_media >= 500 and venda_media < 1200 or preco_atual >= 30 and preco_atual < 80:
    novo_preco = preco_atual + ((15/100) * preco_atual)
elif venda_media >= 1200 or preco_atual >= 80:
    novo_preco = preco_atual - ((20/100) * preco_atual)

print(f"O produto que custava R$ {preco_atual:.2f} agora passou a custar R$ {novo_preco:.2f}")