num = []
pares = [] 
impares = []
cont_par = cont_impar = 0

for i in range(6):
    num.append(int(input('Digite um número inteiro: ')))

for i in range(6):
    if num[i] % 2 == 0:
        pares.append(num[i])
        cont_par += 1
    else:
        impares.append(num[i])
        cont_impar += 1

print(f'A quantidade de números pares foi de {cont_par} números, sendo eles {pares}')
print(f'A quantidade de números ímpares foi de {cont_impar} números, sendo eles {impares}')