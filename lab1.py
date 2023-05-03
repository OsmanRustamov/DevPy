from random import randint
def task1():
    return   "Привет, Python!\nПриятно познакомиться."

print(task1())

def task2():
    f"Ticket on {input('Name of movie: ')} in {input('Name of cinema: ')} at {input('time: ')} booked"

print(task2())

def task3():
    nums = list(map(int, input('Enter 3 nums: ').split(' ')))
    sum_of_nums = sum(nums)
    multiply_nums = 1
    for num in nums:
        multiply_nums *= num
    average_nums = multiply_nums / len(nums)

    f"sum of nums = {sum_of_nums}\nmultiplication of nums = {multiply_nums}\naverage nums = {average_nums}"

print(task3())

def task4():
    num = str(randint(99, 1000))
    return f"{', '.join(num)}"

print(task4())

def task5():
    price_in_dollars, price_in_cent, amount = input("Enter price of pie "), input(), input("Enter amount of pies ")
    cost = int(price_in_dollars + price_in_cent) * int(amount)
    return f"to be paid {str(cost)[0] + str(cost)[1]} dollars {str(cost)[2] + str(cost)[3]} cent"

print(task5())