a = int(input('Введите номер столбца 1-й клетки: '))
b = int(input('Введите номер строки 1-й клетки: '))
c = int(input('Введите номер столбца 2-й клетки: '))
d = int(input('Введите номер строки 2-й клетки: '))

if (c==a+2 and d==b+1) or (c==a+2 and d==b-1) or (c==a-2 and d==b+1) or (c==a-2 and d==b-1) or (d==b+2 and c==a+1) or (d==b+2 and c==a-1) or (d==b-2 and c==a+1) or (d==b-2 and c==a-1):
    print('YES')
else:
    print('NO')