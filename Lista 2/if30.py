import sys  

preco = float(input('Informe o valor do produto: R$ '))
tipo = input('Informe o tipo do produto:\n A - alimentação\n L - limpeza\n V - vestuário\n Resposta: ').upper()
refrig = input('Informe se o produto precisa de refrigeração\n S ou N\n Resposta: ').upper()

# Checa se o tipo é válido
if tipo not in "ALV":
    print('Entre com um tipo válido!')
    sys.exit() # Encerra o programa aqui

# Checa a refrigeração
if refrig not in "SN":
    print('Informe a refrigeração de forma correta!')
    sys.exit()

if refrig == "N":
    if tipo == "A":
        if preco < 15:
            adic = 2
        else:
            adic = 5
    
    if tipo == "L":
        if preco < 10:
            adic = 1.50
        else:
            adic = 2.50
    
    if tipo == "V":
        if preco < 30:
            adic = 3
        else:
            adic = 2.50

elif tipo == "A":
    adic = 8
    
else:
     adic = 0

print(f'Esse produto terá um valor adicional de R$ {adic:.2f}')

if preco < 25:
    imposto = preco * 0.05
else:
    imposto = preco * 0.08

print(f'O imposto desse produto é de R$ {imposto:.2f}')

custo = preco + imposto

print(f'O preço de custo é de R$ {custo:.2f}')

if tipo != "A" and refrig != "S":
    desconto = custo * 0.03
else:
    desconto = 0

print(f'O desconto é de R$ {desconto:.2f}')

novo_preco = custo + adic - desconto

print(f'O valor final é de R$ {novo_preco:.2f}')

if novo_preco <= 50:
    print('Barato')
elif novo_preco > 50 and novo_preco < 100:
    print('Normal')
else:
    print('Caro')
    
    
