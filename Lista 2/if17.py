hora_inicio = int(input("Insira a hora inicial do jogo (sem os minutos): "))
minuto_inicio = int(input("Insira o minuto inicial do jogo: "))
hora_final = int(input("Insira a hora final do jogo (sem os minutos): "))
minuto_final = int(input("Insira o minuto final do jogo: "))

if minuto_inicio > minuto_final:
    minuto_final += 60
    hora_final -= 1
if hora_inicio > hora_final:
    hora_final += 24
minuto_duração = minuto_final - minuto_inicio
hora_duração = hora_final - hora_inicio

print(f"Você jogou por {hora_duração} horas e {minuto_duração} minutos.")