for i in range(10):
    idade = int(input('Informe a idade do nadador: '))
    
    if idade >= 5 and idade <= 10:
        print(f'Com {idade} anos você se classifica na cateriga Infantil')
    elif idade > 10 and idade < 18:
        print(f'Com {idade} anos você se classifica na cateriga Juvenil')
    elif idade >= 18:
        print(f'Com {idade} anos você se classifica na cateriga Adulto')
    else:
        print('Você ainda não tem idade suficiente para ser um nadador!')