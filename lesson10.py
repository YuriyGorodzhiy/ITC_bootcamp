# Задача 1: Сложение двух чисел
print("Задача 1: Сложение двух чисел")
def add(a, b):
    return a + b

print(f"add(5, 3) → {add(5, 3)}")
print(f"add(10, 20) → {add(10, 20)}")
print(f"add(-5, 5) → {add(-5, 5)}")


# Задача 2: Конвертер температуры
print("\nЗадача 2: Конвертер температуры")
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

print(f"celsius_to_fahrenheit(0) → {celsius_to_fahrenheit(0)}")
print(f"celsius_to_fahrenheit(25) → {celsius_to_fahrenheit(25)}")
print(f"celsius_to_fahrenheit(100) → {celsius_to_fahrenheit(100)}")
print(f"celsius_to_fahrenheit(-40) → {celsius_to_fahrenheit(-40)}")


# Задача 3: Проверка четности
print("\nЗадача 3: Проверка четности")
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(f"is_even(4) → {is_even(4)}")
print(f"is_even(7) → {is_even(7)}")
print(f"is_even(10) → {is_even(10)}")
print(f"is_even(15) → {is_even(15)}")
print(f"is_even(20) → {is_even(20)}")


# Задача 4: Подсчет гласных букв
print("\nЗадача 4: Подсчет гласных букв")
def count_vowels(text):
    count = 0
    for letter in text:
        if letter in "аеиоуяaeoy":
            count += 1

    return count

print(f"count_vowels('hello') → {count_vowels('hello')}")
print(f"count_vowels('Python') → {count_vowels('Python')}")
print(f"count_vowels('яблоко') → {count_vowels('яблоко')}")


# Задача 5: Квадрат числа
print("\nЗадача 5: Квадрат числа")
def square(x):
    return x**x

print(f"square(2) → {square(2)}")
print(f"square(3) → {square(3)}")
print(f"square(5) → {square(5)}")


# Задача 6: Проверка палиндрома
print("\nЗадача 6: Проверка палиндрома")
def is_palindrome(text):
     if text == text[::-1]:
         return True
     else:
         return False

print(f"is_palindrome('радар') → {is_palindrome('радар')}")
print(f"is_palindrome('уровень') → {is_palindrome('уровень')}")
print(f"is_palindrome('привет') → {is_palindrome('привет')}")
print(f"is_palindrome('топот') → {is_palindrome('топот')}")


# Задача 7: Максимум из двух чисел
print("\nЗадача 7: Максимум из двух чисел")

def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

print(f"max_of_two(5, 9) → {max_of_two(5,9)}")
print(f"max_of_two(15, 3) → {max_of_two(15,3)}")
print(f"max_of_two(10, 10) → {max_of_two(10,10)}")


# Задача 8: Скидка на покупку
print("\nЗадача 8: Скидка на покупку")

def apply_discount(price, discount_percent):
    return price - (price * discount_percent / 100)

print(f"apply_discount(1000, 10) → {apply_discount(1000, 10)} (скидка 10%)")
print(f"apply_discount(500, 20) → {apply_discount(500, 20)} (скидка 20%)")
print(f"apply_discount(2500, 15) → {apply_discount(2500, 15)} (скидка 15%)")


# Задача 9: Умножение трех чисел
print("\nЗадача 9: Умножение трех чисел")
def multiply_three(a, b, c):
    return a * b * c

print(f"multiply_three(2, 3, 4) → {multiply_three(2, 3, 4)}")
print(f"multiply_three(5, 2, 3) → {multiply_three(5, 2, 3)}")
print(f"multiply_three(1, 1, 1) → {multiply_three(1, 1, 1)}")


# Задача 10: Возрастная категория
print("Задача 10: Возрастная категория")
def get_age_category(age):
    if age < 13:
        return "Ребенок"
    elif 13 <= age <= 17:
        return "Подросток"
    elif 18 <= age <= 65:
        return "Взрослый"
    elif age > 65:
        return "Пенсионер"

print(f"get_age_category(8) → {get_age_category(8)}")
print(f"get_age_category(15) → {get_age_category(15)}")
print(f"get_age_category(25) → {get_age_category(25)}")
print(f"get_age_category(70) → {get_age_category(70)}")