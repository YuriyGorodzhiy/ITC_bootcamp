#  Задача 1: Калькулятор оценок
print("Задача 1: Калькулятор оценок")
mark = int(input("Введите балл от 0 до 100: "))

if mark >= 90 and mark <= 100:
    print("Оценка А")
elif mark >= 80 and mark <= 89:
    print("Оценка B")
elif mark >= 70 and mark <= 79:
    print("Оценка C")
elif mark >= 60 and mark <= 69:
    print("Оценка D")
else:
    print("Оценка F")


# Задача 2: Проверка возрастных ограничений
print("\nЗадача 2: Проверка возрастных ограничений")
age = int(input("Введите возраст: "))

if age < 13:
    print("Ребёнок")
elif age >= 13 and age <= 17:
    print("Подросток")
elif age >= 18 and age <= 64:
    print("Взрослый")
else:
    print("Пенсионер")


# Задача 3: Шифр четности
print("\nЗадача 3: Шифр четности")
number = int(input("Введите число: "))

if number % 2 == 0:
    print(f"Число {number} чётное.")
else:
    print(f"Число {number} нечётное.")


# Задача 4: Проверка входа в систему
print("\nЗадача 4: Проверка входа в систему")

log = input("Введите логин: ")
password = input("Введите пароль: ")

if log == "admin" and password == "12345":
    print("Вход выполнен успешно")
else:
    print("еверный логин или пароль")


# Задача 5: Определение времени суток
print("\nЗадача 5: Определение времени суток")

hour = int(input("Введите час от 0 до 23: "))

if hour >= 0  and hour <= 11:
    print("Утро")
elif hour >= 12 and hour <= 17:
    print("День")
else:
    print("Вечер/Ночь")


# Задача 6: Проверка диапазона температуры
print("\nЗадача 6: Проверка диапазона температуры")

temp = int(input("Введите температуру: "))

if temp < 0:
    print("Холодно")
elif temp >= 0  and temp <= 15:
    print("Прохладно")
elif temp >= 16  and temp <= 25:
    print("Комфортно")
else:
    print("Жарко")


# Задача 7: Проверка скорости (штраф за превышение)
print("\nЗадача 7: Проверка скорости (штраф за превышение)")

speed = int(input("Введите скорость автомобиля: "))

if speed <= 60:
    print("Скорость в норме")
elif speed > 60 and speed <= 80:
    print("Предупреждение")    
else:
    print("Штраф 500 тенге")     


# Задача 8: Проверка возможности получения кредита
print("\nЗадача 8: Проверка возможности получения кредита")

age = int(input("Введите возраст: "))
income = int(input("Введите доход: "))
if age >= 21 and income >= 50000:
    print("Кредит одобрен")
else:
    print("В кредите отказано")


# Задача 9: Определение размера скидки
print("\nЗадача 9: Определение размера скидки")

sum_pay = int(input("Введите сумму покупки: "))

if sum_pay < 1000:
    print(sum_pay)
elif sum_pay >= 1000 and sum_pay < 5000:
    print(sum_pay * (100 - 5) / 100)
elif sum_pay >= 5000 and sum_pay < 10000:
    print(sum_pay * (100 - 10) / 100)
else:
    print(sum_pay * (100 - 15) / 100)


# Задача 10: Проверка валидности возраста и стажа работы
print("\nЗадача 10: Проверка валидности возраста и стажа работы")

age = int(input("Введите возраст: "))
work_expirience  = int(input("Введите cтаж: "))

if age >= 25 and work_expirience >= 3:
    print("Вы можете работать менеджером")
elif age >= 25 and work_expirience < 3:
    print("Вам нужен стаж минимум 3 года")
elif age < 25 and work_expirience >= 3:
    print("Вам нужно быть старше 25 лет")
else:
    print("К сожалению, вы не подходите")