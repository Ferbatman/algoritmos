ano_nasc = int(input('Informe o seu ano de nascimento: '))
ano_atual = int(input('Informe o ano atual: '))

idade = ano_atual - ano_nasc
meses = idade * 12
print(f'A sua idade em {ano_atual} é de {idade} anos.')
print(f'A sua idade em meses no ano de {ano_atual} é de {meses} meses.')