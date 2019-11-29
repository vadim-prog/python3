a = int(input('Введите номер столбца 1-й клетки: '))
b = int(input('Введите номер строки 1-й клетки: '))
c = int(input('Введите номер столбца 2-й клетки: '))
d = int(input('Введите номер строки 2-й клетки: '))

if (c == a + 1 and d == b) or (c == a - 1 and d == b) or (d == b + 1 and c == a) or (
        d == b - 1 and c == a) or d == b or a == c:
    print('No')
else:
    print('Yes')
