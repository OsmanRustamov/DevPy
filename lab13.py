def task1(number_line, line):
    number_line = list(map(int, number_line.split(" ")))
    line = line.split(" ")
    new_line = ""
    for num in number_line:
        new_line += line[num] + " "
    return new_line.capitalize()

print(task1("0 2 1", "zero two one"))

def task2(line):
    words = line.split()
    words.reverse()
    return ' '.join('+'.join(word) for word in words)

print(task2("qwe asd"))
