def is_prime(func):

    def wrapper(*args):
        symma = func(*args)
        print(symma)
        k = 0
        for i in range(2, symma):
            if symma % i == 0:
                k += 1
        if k > 0:
            return f'Составное'
        else:
            return f'Простое'
    return wrapper

@is_prime
def sum_three(a, b, c):
    sym = a + b + c
    return sym

result = sum_three(2, 3, 6)
print(result)