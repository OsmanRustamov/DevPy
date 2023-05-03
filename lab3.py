def task1():
    first_num = int(input("Enter first number "))
    second_num = int(input("Enter second number "))
    if first_num // second_num == 0:
        return "First division on second"
    return "First not division on second"

print(task1())

def task2(*args):
    count = 0
    for i in args:
        if i < 100 and i > 9:
            count += 1
    return count

print(task2(1, 10, 100, 99))