def task1(line1, line2):
    if line1[-1] == line2[0]:
        return "ВЕРНО"
    elif line1[-1] != line2[0]:
        return "НЕВЕРНО"
print(task1('asd', 'dqwe'))

def task2(line, subline1, subline2):
    if subline1 in line:
        line = line.replace(subline1, subline2)
    return line
print(task2("asd", "s", "w"))