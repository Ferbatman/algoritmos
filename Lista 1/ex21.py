Z = float(input("Digite aqui o tamanho da escada: "))
X = float(input("Digite aqui a altura que deseja pregar o quadro: "))

Y = Z ** 2 - X ** 2
Y = Y **(1/2)

print("A distância que a escada deve estar da parede é de {:.1f} metros".format(Y))