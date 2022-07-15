a = input('Введите знающий язык программирования: ')
b = int(input('Введите возраст: '))
c = int(input('Введите опыт работы: '))
d = int(input('Введите желаемую зарплату: '))
if a == 'java' or 'javascript' or 'python':
    print(':)')
else:
    print(':(')
if b >= 18 and b <= 65:
    print(':)')
else:
    print(':(')
if c >= 3:
    print(':)')
else:
    print(':(')
if d <= 60000:
    print(':)')
else:
    print(':(')
