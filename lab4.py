def taks1(num):
    if num > 0:
        return "+"
    elif num < 0:
        return "-"
    else:
        return "0"

def task2(a, b, c):
    i = int(input("Enter variable i: "))
    if i < 4:
        return (a / i) + (b * i**2) + c
    elif i >= 4 and i < 6:
        return i
    elif i > 6:
        return (a * i) + (b * i**3)

print(task2(2.1, 1.8, -20.5))