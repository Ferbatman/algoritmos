angulo = float(input("Informe a medida, em graus, do angulo formado entre escada e o chão: "))
altura = float(input("informe aqui a altura da parede em metros: "))

import math
radiano = angulo * math.pi / 180
escada = altura / math.sin(radiano)

print("A medida dessa escada é de aproximadamente {:.1f} metros".format(escada))