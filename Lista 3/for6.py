maior = menor = 0

for i in range(10):
    idade = int(input('Quanto anos vc tem? '))
    if idade >= 18:
        maior += 1 
    else:
        menor += 1

print(f'Dessas 10 pessoas, {maior} são maiores de idade e {menor} são menores de idade.')