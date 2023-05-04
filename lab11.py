def task1():
    n = int(input("Enter number of marks: "))
    marks = []
    for mark in range(n):
        marks.append(int(input("Enter mark: ")))
    return f"Marks: {' '.join(map(str, marks))}\nAverage mark is {sum(marks) / len(marks)}"

print(task1())

def task2(*x):
    return f"{' '.join(list(map(str, filter(lambda i: i > 0 and i < 1, x))))}"

print(task2(1, 2, 3, 0.1, -1, 0.6, 0.2344, 0.324))

def task3(*x):
    return f"Positive numbers: {list(filter(lambda i: i > 0, x))}\nNegative numbers: {list(filter(lambda i: i < 0, x))}"

print(task3(1, 2, -1, 0, 4, 0, -3))
