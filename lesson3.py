# Задача 1: Преобразование текста
print("Задача 1: Преобразование текста")
text = input("Ввелите любой текст: ")
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())


# Задача 2: Проверка содержимого строки
print("Задача 2: Проверка содержимого строки")
string_input = input("Введите строку: ")
print(string_input.isalpha())
print(string_input.isdigit())
print(len(string_input))


# Задача 3: Замена текста
print("Задача 3: Замена текста")
proposal = input("Введите предложение: ")
replac_word = input("Введите слово для замены: ")
new_word = input("Введите новое слово: ")
new_proposal = proposal.replace(replac_word, new_word)
print(new_proposal)
print(new_proposal.count(new_word))


# Задача 4: Разделение и объединение строк
print("Задача 4: Разделение и объединение строк")
any_words = input("Введите несколько слов через пробел: ")
print(len(any_words.split()))
print("-".join(any_words.split()))


# Задача 5: Проверка начала и конца строки
print("Задача 5: Проверка начала и конца строки")
name_fail = input("Введите имя файла: ")
if name_fail.lower().startswith("а") and name_fail.endswith('.txt'):
    print("Имя файла начинает на 'а' и заканчивается на '.txt'")
else:
    print("Имя файла НЕ начинает на 'а' и НЕ заканчивается на '.txt'")


# Задача 6: Работа со списком студентов
print("Задача 6: Работа со списком студентов")
names_students = ["ПЕтя", "Коля", "Ербол", "Гульнара", "Иван"]
print(names_students)
names_students.append("Юрий")
names_students.extend(["Кира", "Виоллета", "Максим"])
print(names_students)
print(len(names_students))


# Задача 7: Удаление и поиск в списке
print("Задача 7: Удаление и поиск в списке")
fructs = ['яблоко', 'банан', 'апельсин', 'груша', 'банан']
print(fructs)
print(fructs.index("апельсина"))
print(fructs.count('банан'))
print(fructs.remove('банан'))


# Задача 8: Сортировка и разворот списка
print("Задача 8: Сортировка и разворот списка")
list_nums = [5, 2, 9, 1, 7, 3]
print(list_nums)
print(list_nums.sort)
print(list_nums.reverse())


# Задача 9: Вставка и удаление элементов
print("Задача 9: Вставка и удаление элементов")
alphabet =  ['А', 'Б', 'Г', 'Д']
print(alphabet)
alphabet.insert(alphabet.index("Г"), "В")
print(alphabet)
alphabet.pop(1)
print(alphabet)


# Задача 10: Объединение методов строк и списков
print("Задача 10: Объединение методов строк и списков")
string_input = input("Введите предложение со словами через пробел: ")
words = string_input.lower().split()
print(words.sort())
print(", ".join(words))