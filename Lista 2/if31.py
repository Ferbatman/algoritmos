angulo = int(input('Insira aqui um valor de ângulo em graus: '))

if angulo > 360 or angulo < -360:
    voltas = angulo // 360 
    angulo = angulo % 360
else:
    voltas = 0

if angulo == 0 or angulo == 90 or angulo == 180 or angulo == 270 or angulo == 360 or angulo == -90 or angulo == -180 or angulo == -270 or angulo == -360:
    print('Está em cima de algum dos eixos')

if (angulo > 0 and angulo < 90) or (angulo < -270 and angulo > -360):
    print('1º Quadrante')
elif (angulo > 90 and angulo < 180) or (angulo < -180 and angulo > -270):
    print('2º Quadrante')
elif (angulo > 180 and angulo < 270) or (angulo < -90 and angulo > -180):
    print('3º Quadrante')
elif (angulo > 270 and angulo < 360) or (angulo < -0 and angulo > -90):
    print('4º Quadrante')

if angulo < 0:
    sentido = "horário"
else:
    sentido = "anti-horário"

print(f'{voltas} volta(s) no sentido {sentido}')