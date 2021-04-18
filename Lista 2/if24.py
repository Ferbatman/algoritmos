x = float(input('Insira o comprimento de um dos lados do triângulo: '))
y = float(input('Insira o comprimento do outro lado do triângulo: '))
z = float(input('Insira o comprimento do outro lado do triângulo: '))

if x < y + z and y < x + z and z < x + y:
    if x == y and y == z:
        print('Triângulo Equilátero')
    elif x == y or x == z or y == z:
        print('Tirângulo Isóceles')
    elif x != y and x != z and y != z:
        print('Triângulo Escaleno')
    else:
        print('Essas medidas não formam um triângulo.')
