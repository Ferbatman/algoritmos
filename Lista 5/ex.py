idade = [] # declaração do vetor chamado idade vazio

soma_idade = 0

for i in range(5):

    idade.append(int(input('Digite a idade ')))

    soma_idade = soma_idade + idade[i]

media = soma_idade / len(idade)

print('A média de idade é',media)

print('A soma das idades é',soma_idade)

print('Quantidade de elementos',len(idade))

print('Valor da variável i',i)

print(idade)