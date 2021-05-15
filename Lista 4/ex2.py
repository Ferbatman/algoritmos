ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o seu ano de nascimento: "))

while ano_nascimento > 0:
    idade = ano_atual - ano_nascimento
    print(f'Sua idade é de {idade} anos.')
    ano_nascimento = int(input("Digite o seu ano de nascimento: "))