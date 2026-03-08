from datetime import date

today = date.today()

print(f'Hoy es {today}')
print(f'Año es {today.year}')
print(f'Mes es {today.month}')
print(f'Dia es {today.day}')

birthdat = date(1999, 10, 10)
print(f"Cumpleaños es {birthdat}")