nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"{nome} tem {idade} anos, portanto é maior de idade.")
else:
    print(f"{nome} tem {idade} anos, portanto é menor de idade.")
