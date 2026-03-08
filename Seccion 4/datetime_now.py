import locale
from  datetime import datetime

now = datetime.now()
print(f'La fecha acutal es {now}')

date_time = datetime(2019,10,10,14,11,24)
print(date_time.year)

date_format = date_time.strftime('%d/%m/%Y %H:%M')
print(date_format)

locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')

date_format = date_time.strftime('%d de %B, %Y')
print(date_format)
