total_idade = total_homens = total_mulheres = 0

for i in range (1,7):
    qnt_m = qnt_f = x = 0
    resp = 'S'
    print(f"ADS Módulo {i}")
    while resp == 'S':
        sexo = input("Informe seu sexo (M/F): ").strip().upper()[0]
        if sexo not in 'MF':
            print('Categoria não válida!')
        else:
            idade = int(input('Informe sua idade: '))
            if sexo == 'M':
                qnt_m += 1
            elif sexo == 'F':
                qnt_f += 1
        x += idade
        resp = input("Deseja continuar neste Módulo? (S/N) ").strip().upper()[0]
    media = x / (qnt_f + qnt_m)
    print(f'\nNo Módulo {i} de ADS existem {qnt_m} homens e {qnt_f} mulheres. \nA média de idade do Módulo {i} é de {media:.0f} anos.\n')
    total_idade += x   
    total_homens += qnt_m 
    total_mulheres += qnt_f

media_total = total_idade / (total_homens + total_mulheres)

print(f'No curso de ADS existem um total de {total_homens} homens e {total_mulheres} mulheres.\nA média de idade total do curso é de {media_total:.0f} anos.')


