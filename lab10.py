def task1(nums1, nums2):
    unique_numbers = list(map(str, nums1.union(nums2)))
    common_numbers = sorted(list(map(str, nums1.intersection(nums2))))
    return f"unique_numbers = {' '.join(unique_numbers)}\ncommon_numbers = {' '.join(common_numbers)}"
print(task1({1, 2, 3, 4}, {4, 5, 6, 7}))

def task2(line):
    punctuations = set()
    letters = set()

    for char in line:
        if char in ".,;:?!-":
            punctuations.add(char)
        elif char >= "E" and char <= "N":
            letters.add(char)

    result = punctuations.union(letters)

    return f"Множество знаков препинания и букв от E до N: {result}"

print(task2())
