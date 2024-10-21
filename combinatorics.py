
# Факториал
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)



# Формула количества перестановок
def P(n):
    return n * factorial(n -1)


# Формула количества сочетаний 
def C(m, n):
    return factorial(n) / (factorial(n - m) * factorial(m))


# Формула количества размещений
def CP(m, n):
    return factorial(n) / factorial(n-m)


if __name__ != "__main__":
    print("Запустите math_main.")