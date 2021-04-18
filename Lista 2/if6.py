saldo_medio = float(input("Informe o saldo médio no seu último ano: "))

if saldo_medio >= 0 and saldo_medio <= 200:
    credito_especial = 0

elif saldo_medio >= 201 and saldo_medio <= 400:
    credito_especial = saldo_medio * (20/100)

elif saldo_medio >= 401 and saldo_medio <= 600:
    credito_especial = saldo_medio * (30/100)
    
else:
    credito_especial = saldo_medio * (40/100)
    
print(f"Seu saldo médio no último ano foi de R$ {saldo_medio:.2f}, seu crédito especial é de R$ {credito_especial:.2f}")
