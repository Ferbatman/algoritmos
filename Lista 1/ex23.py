numero = float(input("Digite aqui um número real: "))

parte_inteira = numero // 1 #isso retorna um float
parte_fracionaria = round(numero - parte_inteira, 2)
numero_arredondado = round(numero, 0)

print("A parte inteira do número {} é {}".format(numero, parte_inteira))
print("A parte fracionária do número {} é {}".format(numero, parte_fracionaria))
print("O arredondamento do número {} é {}". format(numero, numero_arredondado))