# Напишите программу, которая принимает две строки вида “a/b” - дробь с
# числителем и знаменателем. Программа должна возвращать сумму и произведение*
# дробей. Для проверки своего кода используйте модуль fractions.


import fractions

fract_1 = input("Введите первую дробь в формате a/b: ").split("/")
fract_2 = input("Введите вторую дробь в формате c/d: ").split("/")

# sum_of_fractions
denominator_sum = int(fract_1[1]) * int(fract_2[1])
numerator_sum = int(fract_1[0]) * denominator_sum // int(fract_1[1]) + int(fract_2[0]) * denominator_sum // int(
    fract_2[1])
sum_of_fractions = f"{numerator_sum}/{denominator_sum}"

# product_of_fractions
numerator = int(fract_1[0]) * int(fract_2[0])
denominator = int(fract_1[1]) * int(fract_2[1])
product_of_fractions = f"{numerator}/{denominator}"

print(f"\nРезультат сложение дробей: {sum_of_fractions}")
print(f"Результат произведение дробей: {product_of_fractions}")

print("\nПроверка при помощи <fractions>")
f1 = fractions.Fraction(int(fract_1[0]), int(fract_1[1]))
f2 = fractions.Fraction(int(fract_2[0]), int(fract_2[1]))

print(f"сложение = {f1 + f2}")
print(f"произведение = {f1 * f2}")
