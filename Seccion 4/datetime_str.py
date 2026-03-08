import locale
from datetime import datetime

text = '17/04/2025 18:30'

date_time = datetime.strptime(text, '%d/%m/%Y %H:%M')
print(date_time)

locale.setlocale(locale.LC_TIME, 'Spanish_Spain.1252')
date_str = '17 abril, 2025'
format = '%d %B, %Y'
date_obj = datetime.strptime(date_str, format)
print(date_obj)

date_str = '17 de abril, 2025 14:30'
format = '%d de %B, %Y %H:%M'
date_obj = datetime.strptime(date_str, format)
print(date_obj)

date_str = '17 de abril, 2025 - 02:30 pm'
format = '%d de %B, %Y - %I:%M %p'
date_obj = datetime.strptime(date_str, format)
print(date_obj)