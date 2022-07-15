# <= 10000
# Toyota Lexus
# 2004
# 150000
# white grey:
# 2
# left


# 200000
# < 8000
a = input('Введите марку машины: ')
b = int(input('Введите год выпуска: '))
c = int(input('Введите пробег машины: '))
d = input('Введите расцветку машины: ')
e = int(input('Введите максимальное количество хозяев: '))
f = int(input('Введите цену: '))
if a == 'лексус' or  a == 'тойота':
    print(':)')
else:
    print('не не хочу такую')
if c >= 150000 and f <= 100000:
    print(':)')
elif c >= 200000 and f <= 8000:
    print(':)')
else:
    print(':(')
if b >= 2004:
    print(':)')
else:
    print(':(')
if d == 'белый' or d == 'серый':
    print(':)')
else:
    print(':(')
if e <= 2:
    print(':)')
else:
    print(':(')
