peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print(f"Seu IMC é de {IMC:.1f}, você está abaixo do peso.")

elif IMC >= 18.5 and IMC <= 25:
    print(f"Seu IMC é de {IMC:.1f}, você está no peso normal.")

elif IMC > 25 and IMC <= 30:
    print(f"Seu IMC é de {IMC:.1f}, você está acima do peso.")

else:
    print(f"Seu IMC é de {IMC:.1f}, você está obeso.")