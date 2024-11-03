"""
Программа должна работать в цикле while с возможностью выхода (break)
Запрашивать у пользователя любое слово на латинице или кириллице
Считывать строчные и прописные буквы
Вывести общее количество букв в данном слове
Вывести количество согласных и гласных букв 
Вывести процентное соотношение гласных и согласных букв до двух цифр после точки

Например:
Слово: Гиктек 					Слово: geektech
Количество букв: 6				Количество букв: 8
Согласных букв: 4				Согласных букв: 5
Гласных букв: 2				Гласных букв: 3
Гласные/Согласные: 33.33% / 66.67%		Гласные/Согласные: 37.5% / 62.5%
"""

vowels = "e, y, u, i, o, a, у, е, о, а, ы, я, и, ю, э"

while True:
    world = input("Введите ваше слово: ")
    amount_vowels = 0
    amount_consonants = 0

    for i in world:
        if i in vowels:
            amount_vowels += 1

        else:
            amount_consonants += 1

    if world == "stop" or world == "стоп":
        break

    print("Слово: ", world)
    print("Количество букв: ", len(world))
    print("Согласных букв: ", amount_consonants)
    print("Гласных букв: ", amount_vowels)
    print(
        "Гласных/Согласных: ",
        round(amount_vowels * 100 / len(world), 2),
        "/",
        round(amount_consonants * 100 / len(world), 2),
    )
