a = int(input('Введите номер столбца 1-й клетки: '))
b = int(input('Введите номер строки 1-й клетки: '))
c = int(input('Введите номер столбца 2-й клетки: '))
d = int(input('Введите номер строки 2-й клетки: '))

if (c == a + 1 or c == a - 1 or a==c) and (d == b + 1 or d == b - 1 or d==b):
    print('Yes')
else:
    print('No')