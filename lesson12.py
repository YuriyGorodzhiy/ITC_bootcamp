# Задача 1: Функция с обязательными аргументами
from queue import PriorityQueue

print("Задача 1: Функция с обязательными аргументами")
def multiply(a, b):
    return a * b

print(multiply(3, 4))
print(multiply(5, 6))
print(multiply(2, 9))


# Задача 2: Функция с параметром по умолчанию
print("\nЗадача 2: Функция с параметром по умолчанию")
def greet(name, greeting='Привет'):
    return f"{greeting}, {name}!"

print(greet('Алиса'))
print(greet('Боб', 'Привет'))
print(greet('Виктор', 'Добрый день'))


# Задача 3: Функция с несколькими параметрами по умолчанию
print("\nЗадача 3: Функция с несколькими параметрами по умолчанию")
def info(name, age=18, city='Алматы'):
    return f"{name}, {age} лет, {city}"

print(info('Алиса'))
print(info('Боб', 25))
print(info('Виктор', 30, 'Астана'))


# Задача 4: Функция с *args
print("\nЗадача 4: Функция с *args")
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3))
print(sum_numbers(5, 10, 15, 20))
print(sum_numbers(1))
print(sum_numbers(100, 200, 300, 400, 500))


# Задача 5: Функция с *args для вывода элементов
print("\nЗадача 5: Функция с *args для вывода элементов")
def print_items(*args):
    for index, val in enumerate(args):
        print(f"{index + 1}. {val}")

print_items('apple', 'banana', 'cherry')


# Задача 6: Функция с проверкой типов в *args
print("\nЗадача 6: Функция с проверкой типов в *args")
def count_strings(*args):
    count_str = 0
    for arg in args:
        if isinstance(arg, str):
            count_str += 1
    return count_str

print(count_strings('hello', 5, 'world', 10, 'test'))
print(count_strings(1, 2, 3, 4, 5))
print(count_strings('a', 'b', 'c'))


# Задача 7: Функция с kwargs
print("\nЗадача 7: Функция с **kwargs")
def create_person(**kwargs):
    for key, val in kwargs.items():
        print(f"{key}={val}")

create_person(name='Алиса', age=20, city='Алматы')


# Задача 8: Функция с обычными параметрами и *args
print("\nЗадача 8: Функция с обычными параметрами и *args")
def introduce(name, age, *hobbies):
    print(f"Имя: {name}\n"
          f"Возраст: {age}")
    if hobbies:
        print(f'Хобби: {", ".join(hobbies)}')

introduce('Алиса', 20, 'Читать', 'Рисовать', 'Программировать')


# Задача 9: Функция с *args и **kwargs
print("\nЗадача 9: Функция с *args и **kwargs")
def show_data(name, *numbers, **info):
    print(f"Имя: {name}")
    if numbers:
        print(f"Числа: {numbers}")
    if info:
        print(f"Информация:")
        for key, val in info.items():
            print(f"{key}: {val}")

show_data('Али', 10, 20, 30, city='Алматы', job='Engineer')


# Задача 10: Функция с map() и функцией-аргументом
print("\nЗадача 10: Функция с map() и функцией-аргументом")
def apply_operation(operation, *numbers):
    print(list(map(operation,numbers)))

def double(x):
    return x * 2

apply_operation(double, 1, 2, 3, 4, 5)

def square(x):
    return x * 2

apply_operation(square, 1, 2, 3, 4, 5)