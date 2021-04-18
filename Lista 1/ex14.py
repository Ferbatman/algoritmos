ano_nascimento = int(input("Digite aqui seu ano de nascimento: "))
ano_atual = int(input("Digite aqui o ano atual: "))

idade_atual = ano_atual - ano_nascimento
idade_2050 = 2050 - ano_nascimento

print("A sua idade atual é de {} anos.".format(idade_atual))
print("Sua idade em 2050 será {} anos.".format(idade_2050))