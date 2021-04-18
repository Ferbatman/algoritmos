sexo = input("Qual seu sexo? (Coloque M para masculino e F para feminino) ")
altura = float(input("Qual sua altura? "))

if sexo == "M" or sexo == "m":
    peso = (72.7 * altura) - 58
    print(f"Seu peso ideal é de {peso:.1f} kg")
elif sexo == "F" or sexo == "f":
    peso = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é de {peso:.1f} kg")
else:
    print("Insira 'M' ou 'F' para o sexo")
