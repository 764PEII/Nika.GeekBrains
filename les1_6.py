a = int(input('Количество км в первый день: '))
b = int(input('Конечное количество км: '))
i = 1
while a <= b:
    i+=1
    a = a + a/10
    #print(a)
print(i)