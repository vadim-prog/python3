n = int(input('Введите количество минут: '))
day = 3600
if n < day:
    a = n // 60
    b = n % 60
    if a >= 24:
        a = 0
    print(a, ':', b)
else:
    c = (n - 3600) // 60
    d = (n - 3600) % 60
    if c >= 24:
        c = 0
    print(c, ':', d)
