a = float(input('Введите время в секундах: '))
b = 00
c = 00
if a >= 60:
    b = float(a//60)
    a = float(a % 60)

if b >= 60:
    c = float(b // 60)
    b = float(b % 60)

print(c,':',b,':',a)