import random


def task1():
    rows = []
    table = []
    for row in range(1, 10):
        for column in range(1, 10):
            rows.append(row * column)
        rows = list(map(str, rows))
        table.append(rows)

        rows = []
    for i in table:
     print(' '.join(i))

task1()

def task2():
    for i in range(1, 6):
        print("5 " * i)

task2()

def task3():
    for i in range(10):
        random_number = random.randint(-10, 10)
        if random_number < 0:
            pass
        elif random_number == 0:
            return 0
        else:
            print(random_number**2)
task3()