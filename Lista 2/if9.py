nota1 = float(input("Valor da nota 1: "))
nota2 = float(input("Valor da nota 2: "))
nota3 = float(input("Valor da nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 3 and media < 6:
    print(f'Sua média final foi de {media:.1f} \nExame!')
    nota_exame = 12 - media
    print(f"Você precisa tirar a nota {nota_exame:.1f} para ser aprovado.")
elif media >= 0 and media < 3:
    print(f'Sua média final foi de {media:.1f} \nReprovado!')
else:
    print(f'Sua média final foi de {media:.1f} \nAprovado!')