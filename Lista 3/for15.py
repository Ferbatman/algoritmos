media_total = a = e = r = 0 

for i in range(1,7):
    p1 = float(input('Qual foi a nota da primeira prova? '))
    p2 = float(input('Qual foi a nota da segunda prova? '))
    media = (p1 + p2) / 2
    
    if media <= 3:
        print(f'Sua média foi de {media}. Reprovado!')
        r += 1
    elif media > 3 and media < 7:
        print(f'Sua média foi de {media}. Exame!')
        e += 1
    else:
        print(f'Sua média foi de {media}. Aprovado!')
        a += 1
    
    media_total += media

media_total /= 6

print(f'Foram {a} alunos aprovados, {e} alunos de exame, e {r} alunos reprovados ao total. \nA média total da sala foi de {media_total:.1f}') 
