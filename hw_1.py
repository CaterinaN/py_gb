"""
1.Решите квадратное уравнение 5x**2-10*x-400=0 последовательно
сохраняя переменные a, b, c, d, x1 и x2.
"""

# from math import sqrt

# print('Решение квадратного уравнеия вида a*x**2+b*x+c=0')
# a = float(input('введите значение a : '))
# b = float(input('введите значение b : '))
# c = float(input('введите значение c : '))

# d = b ** 2 - 4 * a * c

# if d > 0:
#     x1 = (-b + sqrt(d)) / (2 * a)
#     x2 = (-b - sqrt(d)) / (2 * a)
#     print(f'"Корни уравнения: x1 = {x1:.3f}; x2 = {x2:.3f}')
# elif d == 0:
#     x1 = -b / (2 * a)
#     print(f'"Корень уравнения: x = {x1:.3f}')
# else:
#     print('Уравнение не имеет корней')



"""
2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""

# print('Опредление существования треугольника со сторонами a,b,c')
# a = float(input('введите длину стороны a: '))
# b = float(input('введите длину стороны b: '))
# c = float(input('введите длину стороны c: '))

# if a + c > b and a + b > c and b + c > a:
#     if a == b and b == c:
#         print('Треугольник существует')
#         print('Треугольник равносторонний')
#     elif a == b or a == c or c == b:
#         print('Треугольник существует')
#         print('Треугольник равнобедренный')
#     else:
#         print('Треугольник существует')
#         print('Треугольник разносторонний')
# else:
#     print('Треугольник не существует')


"""
3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""

while True:
    num = int(input('Введите положительное число до 100000: '))
    if num < 1 or num > 100000:
        print('Число не входит в заданный диапазон')
        continue
    else:
        count = 0
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                count += 1
        if count == 0:
            print("Число простое")
            break
        else:
            print("Число составное")
            break