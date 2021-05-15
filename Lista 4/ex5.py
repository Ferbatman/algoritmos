resp = 'S'
qntd_m = qntd_f = m_idade_maior = m_idade_menor = f_idade_maior = f_idade_menor = 0

while resp == 'S':
    sexo = input("Informe seu sexo (M/F): ").strip().upper()[0]
    if sexo not in "MF":
        print("Entre com um sexo válido!")
    
    else:
        idade = int(input("Informe a sua idade: "))

        if sexo == 'M':
            qntd_m += 1
            if idade < 18:
                m_idade_menor += 1
            else:
                m_idade_maior += 1
        
        elif sexo == 'F':
            qntd_f += 1
            if idade < 18:
                f_idade_menor += 1
            else:
                f_idade_maior += 1


    resp = input("Deseja continuar os cadastros? (S/N) ").strip().upper()[0]

print(f'Foram cadastrados {qntd_m} homens e {qntd_f} mulheres no nosso sistema.')
print(f'Sendo um total de {m_idade_menor} homens e {f_idade_menor} mulheres menores de idade, e um total de {m_idade_maior} homens e {f_idade_maior} mulheres maiores de idade.')