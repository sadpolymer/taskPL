#from sys import argv
#script, n, m = argv
n = int(input("Введите длину массива: "))
m = int(input("Введите длину интервала: "))
#Проверка на корректность значений
if n != m:
    if n > 0 and m > 0:
        if n % 2 == 0 and m % 2 == 0:
            print("Оба значения не могут быть чётными")
        else:
            interval = list(range(1, n+1))
            array = interval * 10000000
            #k - индекс элемента массива
            i = 1
            k = 1
            while array[k] != 1:
                i += 1
                k = i * m - 1
            else:
                lst = array[0:k:m]
                print(lst);
    else:
        print("Оба занчения должны быть больше нуля")
else:
    print("Длина массива не может быть равна длине интервала");
