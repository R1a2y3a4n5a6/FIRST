a = input()
print(a[a.rfind('.') + 1:] if '.' in a else 'Что-то с файликом не так')
