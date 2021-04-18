print("A para os 3 itens a seguir informe um valor para cada em ordem crescente!")
numero1 = float(input("Primeiro valor: "))
numero2 = float(input("Segundo valor: "))
numero3 = float(input("terceiro valor: "))
numero4 = float(input("Agora informe um número qualquer: "))

if numero1 > numero2 or numero1 > numero3 or numero2 > numero3:
    print("Você não colocou os três primeiros valores em ordem crescente, por favor faça novamente!")

elif numero4 > numero3:
    print(f"A ordem decrescente é: {numero4}, {numero3}, {numero2}, {numero1}")

elif numero4 > numero2 and numero4 < numero3:
    print(f"A ordem decrescente é: {numero3}, {numero4}, {numero2}, {numero1}")

elif numero4 > numero1 and numero4 < numero2:
    print(f"A ordem decrescente é: {numero3}, {numero2}, {numero4}, {numero1}")

elif numero4 < numero1:
    print(f"A ordem decrescente é: {numero3}, {numero2}, {numero1}, {numero4}")

