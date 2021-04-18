altura_degrau = float(input("Informe, em metros, qual é a altura de cada degrau da escada: "))
altura_desejada = float(input("Informe, em metros, qual é a altura desejada a se chega: "))

quantidade_de_degraus = altura_desejada // altura_degrau

print("Para atingir seu objetivo, você deverá subir {} degraus".format(int(quantidade_de_degraus)))