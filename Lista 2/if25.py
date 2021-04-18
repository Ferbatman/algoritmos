altura = float(input('Coloque sua altura: '))
peso = float(input('Coloque seu peso: '))

if altura < 1.20:
    if peso <= 60:
        print("A")
    elif peso > 60 and peso <= 90:
        print("D")
    else:
        print("G")

elif altura >= 1.20 and altura <= 1.70:
    if peso <= 60:
        print("B")
    elif peso > 60 and peso <= 90:
        print("E")
    else:
        print("H")

elif altura > 1.70:
    if peso <= 60:
        print("C")
    elif peso > 60 and peso <= 90:
        print("F")
    else:
        print("I")