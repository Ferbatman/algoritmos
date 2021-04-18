from datetime import datetime
hoje = datetime.now()

print(f"Ano atual: {hoje.year}")
print(f"Mês: {hoje.month}")
print(f"Dia: {hoje.day}")
print(f"Hora: {hoje.hour}")
print(f"Minutos: {hoje.minute}")
print(f"segundos: {hoje.second}")

if hoje.month == 1:
    print(f"{hoje.day}/{hoje.month}/{hoje.year} - Janeiro {hoje.hour}:{hoje.minute}")
if hoje.month == 2:
    print(f"{hoje.day}/{hoje.month}/{hoje.year} - Fevereiro {hoje.hour}:{hoje.minute}")
if hoje.month == 3:
    print(f"{hoje.day}/{hoje.month}/{hoje.year} - Março {hoje.hour}:{hoje.minute}")