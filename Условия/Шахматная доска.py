a = int(input('Введите номер столбца 1-й клетки: '))
b = int(input('Введите номер строки 1-й клетки: '))
c = int(input('Введите номер столбца 2-й клетки: '))
d = int(input('Введите номер строки 2-й клетки: '))

if ((a % 2 == 0 and b % 2 == 0) or (a % 2 != 0 and b % 2 != 0)) and ((c % 2 == 0 and d % 2 == 0) or (c % 2 != 0 and d % 2 != 0)):
    print('YES')
elif ((a % 2 != 0 and b % 2 == 0) or (a % 2 == 0 and b % 2 != 0)) and ((c % 2 != 0 and d % 2 == 0) or (c % 2 == 0 and d % 2 != 0)):
    print('YES')
else:
    print('NO')
