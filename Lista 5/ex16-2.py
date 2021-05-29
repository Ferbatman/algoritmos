lista1 = [ float( input("Digite um número para a lista 1: " ) ) for i in range(5) ] 
lista2 = [ float( input("Digite um número para a lista 2: " ) ) for i in range(5) ]

lista3 = lista1 + lista2
lista3.sort()

print(f'Vetor 1: {lista1}')
print(f'Vetor 2: {lista2}')
print(f'A junção de ambos vetores em ordem crescente é: {lista3}')