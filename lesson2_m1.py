day = int(input("Введите день вашего рождения: "))

month = int(input("Введите месяц вашего рождения: "))

if day not in range(0, 31) or month not in range(1, 12):
    print("Вы ввели некоректные данные! \n День от 1-31 \n Месяц от 1-12")

if day in range(20, 32) and month == 3 or day in range(0, 21) and month == 4:
    print("Ваш знак зодиака Овен")

elif day in range(20, 31) and month == 4 or day in range(0, 22) and month == 5:
    print("Ваш знак зодиака Телец")

elif day in range(21, 32) and month == 5 or day in range(0, 22) and month == 6:
    print("Ваш знак зодиака Близнецы")

elif day in range(21, 31) and month == 6 or day in range(0, 23) and month == 7:
    print("Ваш знак зодиака Рак")

elif day in range(22, 32) and month == 7 or day in range(0, 22) and month == 8:
    print("Ваш знак зодиака Лев")

elif day in range(23, 32) and month == 8 or day in range(0, 24) and month == 9:
    print("Ваш знак зодиака Дева")

elif day in range(23, 31) and month == 9 or day in range(0,
                                                         24) and month == 10:
    print("Ваш знак зодиака Весы")

elif day in range(23, 32) and month == 10 or day in range(0,
                                                          23) and month == 11:
    print("Ваш знак зодиака Скорпион")

elif day in range(22, 31) and month == 11 or day in range(0,
                                                          23) and month == 12:
    print("Ваш знак зодиака Стрелец")

elif day in range(22, 32) and month == 12 or day in range(0,
                                                          21) and month == 4:
    print("Ваш знак зодиака Козерог")

elif day in range(19, 32) and month == 1 or day in range(0, 20) and month == 2:
    print("Ваш знак зодиака Водолей")

elif day in range(19, 30) and month == 2 or day in range(0, 21) and month == 3:
    print("Ваш знак зодиака Рыбы")

else:
    print("Вы ввели не правильную дату")
