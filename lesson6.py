# Задача 1: Простой счетчик
print("Задача 1: Простой счетчик")
num = int(input("Введите число N: "))
num_i = 1
while num_i <= num:
    print(num_i)
    num_i += 1


# Задача 2: Обратный отсчет
print("\nЗадача 2: Обратный отсчет")
num = int(input("Введите число N: "))
while num > 0:
    print(num)
    num -= 1


# Задача 3: Сумма чисел
print("\nЗадача 3: Сумма чисел")
num = int(input("Введите число N: "))
summ = 0
num_i = 1
while num_i <= num:
    summ += num_i
    num_i += 1
print(f"Сумма от 1 до {num} = {summ}")


# Задача 4: Перебор списка с индексом
print("\nЗадача 4: Перебор списка с индексом")
list_num = [10, 20, 30, 40, 50]
ind = 0
while ind < len(list_num):
    print(f"Индекс {ind}: {list_num[ind]}")
    ind += 1


# Задача 5: Поиск элемента в списке
print("\nЗадача 5: Поиск элемента в списке")
list_language = ['Python', 'Java', 'C++', 'JavaScript', 'Go']
lng_prog = input("Введите язык программирования: ")
iter = 0
while iter < len(list_language):
    if lng_prog == list_language[iter]:
        print(f"{list_language[iter]} - индекс {iter}")
    iter += 1
else:
    print("Язык не найден")


# Задача 6: Произведение чисел
print("\nЗадача 6: Произведение чисел")
num = int(input("Введите число N: "))
num_i = 2
prod_nums = 1
while num_i <= num:
    prod_nums *= num_i
    num_i += 1
print(f"Произведение чисел от 1 до {num} равно {prod_nums}")


# Задача 7: Четные числа в диапазоне
print("\nЗадача 7: Четные числа в диапазоне")
start = int(input("Введите число start: "))
end = int(input("Введите число end: "))
count_nums = 0
while start <= end:
    if start % 2 == 0:
        print(start)
        count_nums += 1
    start += 1
print(f"Количество чётных чисел: {count_nums}")


# Задача 8: Проверка пароля с ограничением попыток
print("\nЗадача 8: Проверка пароля с ограничением попыток")
pass_right = 'qwerty'
count_input = 1
while count_input < 4:
    pass_input = input("Введите пароль: ")
    if pass_input == pass_right:
        print("Пароль верный!")
        break
    else:
        print(f"Попытка {count_input} из 3")
    count_input += 1
else:
    print("Доступ запрещен")


# Задача 9: Сумма положительных чисел
print("\nЗадача 9: Сумма положительных чисел")
summ = 0
count = 0
while True:
    num = int(input("Введите число: "))
    if num > 0:
        summ += num
        count += 1
    else:
        break
print(f"Сумма чисел - {summ}, количество чисел - {count}")


# Задача 10: Уменьшение числа в два раза
print("\nЗадача 10: Уменьшение числа в два раза")
num = int(input("Введите число N: "))
while num >= 1:
    print(num)
    num /= 2