print("1 - Imposto \n2 - Novo Salário \n3 - Classificação")
a = int(input("Escolha uma das opções: "))

if a == 1:
    salario = float(input("Insira o valor do seu salário: "))
    if salario < 500:
        imposto = salario * 0.05
    elif salario >= 500 and salario <= 850:
        imposto = salario * 0.10
    else:
        imposto = salario * 0.15
    print(f"Seu imposto é de R$ {imposto:.2f}")

elif a == 2:
    salario = float(input("Insira o valor do seu salário: "))
    if salario > 1500:
        salario += 25
    elif salario >= 750 and salario <= 1500:
        salario += 50
    elif salario >= 450 and salario < 750:
        salario += 75
    else:
        salario += 100
    print(f"Seu novo salário é de R$ {salario:.2f}")

elif a == 3:
    salario = float(input("Insira o valor do seu salário: "))
    if salario <= 700:
        print("Seu salário está classificado como Mal Remunerado!")
    else:
        print("Seu salário está classificado como Bem Remunerado!")

else:
    print("Essa opção é inválida, por favor entre com outra opção.")