trabalho = float(input("Informe a nota do trabalho de laboratório: "))
avaliacao = float(input("Informe a nota da avaliação semestral: "))
exame = float(input("Informe a nota do exame final: "))

media_ponderada = ((trabalho * 2) + (avaliacao * 3) + (exame *5)) / 10

if media_ponderada >= 8.0 and media_ponderada <= 10:
    n = "A"
elif media_ponderada >= 7.0 and media_ponderada < 8:
    n = "B"
elif media_ponderada >= 6.0 and media_ponderada < 7:
    n = "C"
elif media_ponderada >= 5.0 and media_ponderada < 6:
    n = "D"
else:
    n = "E"

print(f"Sua média ponderada é de {media_ponderada:.1f}, seu conceito é '{n}'.")