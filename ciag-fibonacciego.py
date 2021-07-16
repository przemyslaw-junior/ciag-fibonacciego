# ciąg fibonacciego
'''
fib1 = 1
fib2 = 1
fib3 = 1 + 1 = 2
fib4 = 1 + 2 = 3
fib5 = 2 + 3 = 5
fib6 = 3 + 5 = 8
fib7 = 5 + 8 = 13
'''
# nr 1
def fib_1(n):
    wynik = [1, 1]
    for i in range(n-2):
        wynik.append(wynik[i] + wynik[(i + 1)])

    return wynik

print (fib_1(10))

# nr 2
def fib_2(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem1 = elem2 = 1
    suma = 0
    for i in range(3, n + 1):
        suma = elem1 + elem2
        elem1, elem2 = elem2, suma
    return suma

for n in range(1, 11): # test
    print(n, "->", fib_2(n))

# nr 3
def fib_3(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib_3(n - 1) + fib_3(n - 2)
