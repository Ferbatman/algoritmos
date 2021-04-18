ano_atual = int(input("Digite o ano atual: "))

salario_inicial = 1000
perc_aumento = 1.5 / 100
aumento_ano = salario_inicial * perc_aumento
salario_ano = salario_inicial + aumento_ano

for i in range (2007, ano_atual + 1):
    perc_aumento *= 2
    salario_ano = salario_ano * (1 + perc_aumento) # a * (b + c) = a * b + a * c
    
print(f"Em {ano_atual} seu salário é de R$ {salario_ano:.2f}")
  