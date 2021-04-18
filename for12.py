maior = menor = 0

for i in range(1,21):
    valor = float(input('Informe o preço da TV: '))
    if i == 1:
        maior = menor = valor
    elif valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor

print(f"A TV com o maior valor foi de R$ {maior:.2f} e a TV de menor valor foi de R$ {menor:.2f}") 