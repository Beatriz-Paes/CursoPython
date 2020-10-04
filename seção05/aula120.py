# Datetime - Trabalhando com data e hora

from datetime import datetime, timedelta

# data = datetime(2020, 10, 3, 23, 55, 20)
#
# print(data.strftime('%d/%m/%Y %H:%M:%S'))
#
# data1 = datetime.strptime('04/10/2020', '%d/%m/%Y')
# print(data1.timestamp())
#
# data2 = datetime.fromtimestamp(1601784000.0)
# print(data2)

#################################################################

data = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')

# Adicionar 5 dias a data:

data = data + timedelta(days=5, seconds=20)
print(data.strftime('%d/%m/%Y %H:%M:%S'))

#################################################################

d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')

dif = d2 - d1

print(dif)
print(dif.seconds)
print(dif.total_seconds())
print(dif.days)

print(d2 > d1)
