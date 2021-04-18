idade = int(input("Digite sua idade: "))

if idade >= 5 and idade <= 10:
    print(f"Você tem {idade} anos, sua categoria de nadador é infantil")
elif idade >= 11 and idade <= 17:
    print(f"Você tem {idade} anos, sua categoria de nadador é juvenil")
elif idade >= 18:
    print(f"Você tem {idade} anos, sua categoria de nadador é adulto")
else:
    print(f"Você tem ainda não tem idade para nadar!")
