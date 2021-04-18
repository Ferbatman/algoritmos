maior = menor = 0

for i in range(1,11):
    nome = input("Qual seu nome? ")
    altura = float(input('Qual sua altura? '))
    if i == 1:
        maior = menor = altura
        nome1 = nome2 = nome
    elif altura > maior:
        maior = altura
        nome1 = nome
    elif altura < menor:
        menor = altura
        nome2 = nome

print(f"{nome1} tem a maior altura medindo {maior:.2f} metros de altura, e {nome2} tem a menor altura medindo {menor:.2f} metros de altura.") 