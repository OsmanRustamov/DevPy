def task1(line):
    if " " in line:
        return line[::-1]

print(task1('qwe rty'))

def task2(line):
    count = 0
    if ":" in line:
        count += 1
        line = line.replace(":", "")
    return f"{line} count = {count}"

print(task2('asd:qwe'))