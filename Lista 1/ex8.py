deposito = float(input("Coloque aqui o valor que você deseja depositar: "))

taxa = float(input("Coloque aqui o valor da taxa de juros: "))

rendimento = deposito * taxa / 100
total = deposito + rendimento

print("O valor do rendimento é de R$ {:.2f}".format(rendimento))

print("O valor total do rendimento de um mês é de R$ {:.2f}".format(total))
