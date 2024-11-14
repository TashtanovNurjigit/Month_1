data_tuple = ("h", 6.13, "C", "e", "T", True, "k", "e", 3, "e", 1, "g")

letters = []
numbers = []

for i in data_tuple:
    if type(i) in [str, bool]:
        letters.append(i)

    else:
        numbers.append(i)

numbers.remove(6.13)
numbers.insert(1, 2)
numbers.sort()
numbers = tuple(i**2 for i in numbers)

copy_letters = letters
for i in copy_letters:
    if i is True:
        letters.remove(i)
        letters.append(i)

letters.reverse()
letters[1], letters[-2] = "G", "c"
letters = tuple(letters)
print(numbers, letters)
