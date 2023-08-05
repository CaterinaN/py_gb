"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака."""

goods = {"Спальник": 3, "Котел": 2, "Куртка": 0.7, "Аптечка": 1, "Консервы": 1.5, "Тарелка": 0.2,
         "Гречка": 2, "Вода": 3, "Палатка": 3.5, "Зубная паста": 0.1}
all_size = float(input("Введите максимальную грузоподъёмность рюкзака : "))

print(f"Список вещей и их вес - {goods}")

weight = 0
stock_lst = []
for key, value in goods.items():
    weight += value

if weight > all_size:
    size = all_size
    weight = 0
    for key, value in goods.items():
        if value <= size:
            size -= value
            weight += value
            stock_lst.append(key)

    surplus = []
    for elem in goods:
        if elem not in stock_lst:
            surplus.append(elem)
    print(f"Поместилось в рюкзак {stock_lst}. Не поместилось {surplus}")

else:
    print(f"Вместимость рюкзака: {all_size}! Поздравляю,можешь взять все вещи!")
