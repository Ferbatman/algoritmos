numero_1 = float(input("Insira um número: "))
numero_2 = float(input("Insira outro número: "))
numero_3 = float(input("Insira outro número: "))

if numero_1 < numero_2 and numero_1 < numero_3:
    if numero_2 < numero_3:
        print(f"A ordem crescente é: {numero_1}, {numero_2}, {numero_3}")
    else:
        print(f"A ordem crescente é: {numero_1}, {numero_3}, {numero_2}")

if numero_2 < numero_1 and numero_2 < numero_3:
    if numero_1 < numero_3:
        print(f"A ordem crescente é: {numero_2}, {numero_1}, {numero_3}")
    else:
        print(f"A ordem crescente é: {numero_2}, {numero_3}, {numero_1}")

if numero_3 < numero_1 and numero_3 < numero_2:
    if numero_1 < numero_2:
        print(f"A ordem crescente é: {numero_3}, {numero_1}, {numero_2}")
    else:
        print(f"A ordem crescente é: {numero_3}, {numero_2}, {numero_1}")