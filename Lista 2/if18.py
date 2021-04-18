print("1 - Escriturário \n2 - Secretário \n3 - Caixa \n4 - Gerente \n5 - Diretor")
cargo = int(input("Insira o código do seu cargo: "))
salario = float(input("Informe seu salário atual: "))

if cargo == 1:
    aumento = salario * 0.5
    novo_sal = salario + aumento
    print(f"Seu cargo é de Escriturário, você tem um aumento de R$ {aumento:.2f}, seu novo salário é de R$ {novo_sal:.2f}")
elif cargo == 2:
    aumento = salario * 0.35
    novo_sal = salario + aumento
    print(f"Seu cargo é de Secretário, você tem um aumento de R$ {aumento:.2f}, seu novo salário é de R$ {novo_sal:.2f}")
elif cargo == 3:
    aumento = salario * 0.20
    novo_sal = salario + aumento
    print(f"Seu cargo é de Caixa, você tem um aumento de R$ {aumento:.2f}, seu novo salário é de R$ {novo_sal:.2f}")
elif cargo == 4:
    aumento = salario * 0.10
    novo_sal = salario + aumento
    print(f"Seu cargo é de Gerente, você tem um aumento de R$ {aumento:.2f}, seu novo salário é de R$ {novo_sal:.2f}")
elif cargo == 5:
    aumento = 0
    novo_sal = salario + aumento
    print(f"Seu cargo é de Diretor, você tem um aumento de R$ {aumento:.2f}, seu novo salário é de R$ {novo_sal:.2f}")
