import math

def task1():
    print("Как Вас зовут?")
    name = input()
    print("Добрый день, ", name)
    print("Укажите названия техникума.")
    college = input()
    print("Укажите номер вашей группы.")
    group = input()
    print("Вы обучаетесь в образовательной организации ", college, " в группе ", group)
    print("Какой язык программирования вы начинаете изучать?")
    lang = input()
    print(name, ", желаем Вам успешного обучения программированию на языке ", lang)

task1()

def task2(a, b, x):
    return math.sin((x**2 + a)**2)**3 - (x / b)**0.5

print(task2(1.1, 0.004, 0.2))
