a = int(input('Введите выручку компании '))
b = int(input("Введите сумму издержек компании "))
с = 0
print('Финансовый результат: ', a-b)
if a-b > 0:
    print('Прибыль')
    print('Рентабильность: ', f"{((a-b)/a)*100:.2f}")
    c = int(input("Введите количество сотрудников: "))
    print("Прибыль на одного сотрудника: ", f"{(a-b) / c:.2f}")
elif a-b == 0:
    print('Окупание без прибыли')
elif a-b < 0:
    print('Убыток')