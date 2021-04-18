codigo_produto = int(input("Insira o codigo do produto comprado (numero de 1 até 10): "))
peso = float(input("Insira o peso do produto em KG: "))
codigo_pais = int(input("Insira o codigo do país (numero de 1 até 3):"))

peso_gramas = peso * 1000
print(f"O peso do produto em gramas é de {peso_gramas:.0f}")

if codigo_produto >=1 and codigo_produto <= 4:
    preco_grama = 10
elif codigo_produto >= 5 and codigo_produto <= 7:
    preco_grama = 25
elif codigo_produto >= 8 and codigo_produto <= 10:
    preco_grama = 35

preco_total = peso_gramas * preco_grama
print(f'O preço total foi de R$ {preco_total:.2f}')

if codigo_pais == 1:
    imposto = 0
elif codigo_pais == 2:
    imposto = preco_total * 15/100
elif codigo_pais == 3:
    imposto = preco_total * 25/100
print(f'O imposto do país é de R$ {imposto:.2f}')

valor_total = imposto + preco_total

print(f"O valor final com imposto é de R$ {valor_total:.2f}")