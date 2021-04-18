a = float(input("Entre com um valor: "))
b = float(input("Entre com um valor: "))
c = float(input("Entre com um valor: "))

if a == 0:
    print("Entre com 'a' válido != 0")

else:
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        print("Não existe solução para isso (raiz real)")

    elif delta == 0:
        x = -b / (2 * a)
        print("A solução para equação é:", x)

    else:
        from math import sqrt
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print("As soluções para equação são:", x1, x2)