from . import areas
from . import combinatorics

    number = input('Введите номер нужного модуля: 1) геометрия, 2) комбинаторика')
    if number == 1:
        geo_number = input('Вы выбрали геометрию. Введите номер нужной функции: 1)прямоугольник, 2)квадрат, 3)треугольник, 4) шар')
        if geo_number == 1:
            a_rect = int(input('Введите 1 сторону прямоугольника: '))
            b_rect = int(input('Введите 2 сторону прямоугольника: '))
            print(f'Площадь прямоугольника со сторонами {a_rect} и {b_rect} равна {areas.S_rectangle(a_rect, b_rect)}')
        elif geo_number == 2:
            a_square = int(input('Введите сторону квадрата: '))
            print(f'Площадь квадарата со стороной {a_square} равна {areas.S_square(a_square)}')
        elif geo_number == 3:
            a_triangle = int(input('Введите основание треугольника: '))
            h_triangle = int(input('Введите высоту треугольника: '))
            print(f'Площадь треугольника с основанием {a_triangle} и высотой {h_triangle} равна {areas.S_triangle(a_triangle, h_triangle)}')
        elif geo_number == 4:
            r_sphere = int(input('Введите радиус окружности: '))
            print(f'Площадь окружности с радиусом {r_sphere} равна {areas.S_square(r_sphere)}')
    elif number == 2:
        comb_number = input('Вы выбрали комбинаторику. Введите номер нужной функции: 1)факториал, 2)количество перестановок, 3)количество сочетаний, 4)количество размещений')
        if comb_number == 1:
            number_f = int(input('Введите число: '))
            print(f'Факториал числа {number_f} равен {combinatorics.factorial(number_f)}')
        elif comb_number == 2:
            number_p = int(input('Введите число: '))
            print(f'Количество перестановок числа {number_p} равно {combinatorics.P(number_p)}')
        elif comb_number == 3:
            m_С = int(input('Введите первое число: '))
            n_C = int(input('Введите второе число: '))
            print(f'Количество сочетаний из{ n_C} по {m_С} равно {combinatorics.C(m_С, n_C)}')
        elif comb_number == 4:
            m_CP = int(input('Введите первое число'))
            n_CP = int(input('Введите второе число: '))
            print(f'Количсетво размещений из {n_CP} по {m_CP} равно {combinatorics.CP(m_CP, n_CP)}')
