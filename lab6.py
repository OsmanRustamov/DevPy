def task1(k):
    for num in range(k + 1):
        print("Root of number ", num, "is ", num**0.5, "and cube is ", num**2)

task1(1)

def task2():
    sum_of_cube_numbers = 0
    for num in range(7, 37):
        sum_of_cube_numbers += num**3
    return sum_of_cube_numbers

print(task2())