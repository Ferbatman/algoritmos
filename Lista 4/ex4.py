numero = int(input('Digite um numero inteiro: '))
maior = menor = numero

while numero != 0:
    
    if numero < 0:
        print('Esse numero é negativo')
  
    elif numero < menor:
        menor = numero

    elif numero > maior:
        maior = numero
    
    numero = int(input('Digite um numero inteiro: '))

print(f"O numero de maior valor foi {maior} e o numero de menor valor foi {menor}")