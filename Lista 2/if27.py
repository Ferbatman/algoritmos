codigo_estado = int(input('Digite aqui o codigo do estado de origem da carga (codigo de 1 a 5): '))
peso_carga = float(input("Insira o peso da carga do caminhão em toneladas: "))
codigo_carga = int(input('Digite o codigo da carga (codigo de 10 a 40): '))

peso_kg = peso_carga * 1000
print(f'O peso da carga do caminhão em kg é de {peso_kg:.0f}')

if codigo_carga >= 10 and codigo_carga <= 20:
    preco_carga = peso_kg * 100
elif codigo_carga > 20 and codigo_carga <= 30:
    preco_carga = peso_kg * 250
elif codigo_carga > 30 and codigo_carga <= 40:
    preco_carga = peso_kg * 400
print(f'O preço da carga em kg é de R$ {preco_carga:.2f}')

if codigo_estado == 1:
    imposto = preco_carga * (35/100)
elif codigo_estado == 2:
    imposto = preco_carga * (25/100)
elif codigo_estado == 3:
    imposto = preco_carga * (15/100)
elif codigo_estado == 4:
    imposto = preco_carga * (5/100)
elif codigo_estado == 5:
    imposto = 0
print(f'O valor do imposto do produto neste estado é de R$ {imposto:.2f}')

total = preco_carga + imposto

print(f'O valor total do produto é de R$ {total:.2f}')
