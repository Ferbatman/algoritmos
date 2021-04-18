print("Compare duas datas a seguir")

dia1 = int(input("Insira um dia: "))
mes1 = int(input("Insira um mês (número): "))
ano1 = int(input("Insira um ano: "))

dia2 = int(input("Insira um dia: "))
mes2 = int(input("Insira um mês (número): "))
ano2 = int(input("Insira um ano: "))

if ano1 > ano2:
    print(f"A maior data é: {dia1}/{mes1}/{ano1}")
elif ano2 > ano1:
    print(f"A maior data é: {dia2}/{mes2}/{ano2}")
elif mes1 > mes2:
    print(f"A maior data é: {dia1}/{mes1}/{ano1}")
elif mes2 > mes1:
    print(f"A maior data é: {dia2}/{mes2}/{ano2}")
elif dia1 > dia2:
    print(f"A maior data é: {dia1}/{mes1}/{ano1}")
elif dia2 > dia1:
    print(f"A maior data é: {dia2}/{mes2}/{ano2}")
else:
    print("As datas são iguais!")
