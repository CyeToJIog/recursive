def test(*param):
    print(*param)
    print(param)


test(1, 2, "да", "нет", True, False)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(6))
