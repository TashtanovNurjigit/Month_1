"""
Добавить/расширить список актуальными курсами, которые вы знаете. Затем преобразовать этот список в set
Добавить дату основания Geeks в виде строки
Вывести количество курсов
Вывести словарь на экран с помощью цикла for с получением всех пар 
“ключ: значение”
"""

Geeks = {
    "address": "Toktogula 175",
    "courses": ["Android", "Backend", "Frontend"],
    "bag": {"fails", "errors", "stack"},
}

Geeks.pop("bag")
Geeks["address"] = "Toktogula 93"
Geeks["phone"] = "+996508903902"
Geeks["instagram"] = "geeks_edu"
Geeks["courses"] = ["frontend", "backend", "ux/ui", "android"]
Geeks["courses"] = set(Geeks["courses"])
print(len(Geeks["courses"]))
for key, values in Geeks.items():
    print(f"{key}: {values}")
