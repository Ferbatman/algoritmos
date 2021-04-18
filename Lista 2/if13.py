I = int(input("Digite 1, 2 ou 3: "))
A = float(input("Digite qualquer numero: ")) 
B = float(input("Digite qualquer numero: "))
C = float(input("Digite qualquer numero: "))

if I == 1:
    if A < B and A < C:
        if B < C:
            print(f"A ordem crescente dos numeros é: {A}, {B}, {C}")
        else:
            print(f"A ordem crescente dos numeros é: {A}, {C}, {B}")
    if B < A and B < C:
        if A < C:
            print(f"A ordem crescente dos numeros é: {B}, {A}, {C}")
        else:
            print(f"A ordem crescente dos numeros é: {B}, {C}, {A}")
    if C < A and C < B:
        if A < B:
            print(f"A ordem crescente dos numeros é: {C}, {A}, {B}")
        else:
            print(f"A ordem crescente dos numeros é: {C}, {B}, {A}")
        
if I == 2:
    if A > B and A > C:
        if B > C:
            print(f"A ordem decrescente dos numeros é: {A}, {B}, {C}")
        else:
            print(f"A ordem decrescente dos numeros é: {A}, {C}, {B}")
    if B > A and B > C:
        if A > C:
            print(f"A ordem decrescente dos numeros é: {B}, {A}, {C}")
        else:
            print(f"A ordem decrescente dos numeros é: {B}, {C}, {A}")
    if C > A and C > B:
        if A > B:
            print(f"A ordem decrescente dos numeros é: {C}, {A}, {B}")
        else:
            print(f"A ordem decrescente dos numeros é: {C}, {B}, {A}")

if I == 3:
    if A > B and A > C:
        print(f"A ordem desejada é: {B}, {A}, {C}")
    if B > A and B > C:
        print(f"A ordem desejada é: {A}, {B}, {C}")
    if C > A and C > B:
        print(f"A ordem desejada é: {A}, {C}, {B}")