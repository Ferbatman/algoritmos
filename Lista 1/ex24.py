hora = float(input("Informe a hora exata com minutos: "))

h = hora // 1
minutos = hora - h
conversao = (h * 60) + (minutos * 100)

print("{} horas é equivalente a {} minutos".format(hora, int(conversao)))