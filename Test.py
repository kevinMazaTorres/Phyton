EJERCICIO 1-
def sum_odd_numbers(numbers):
    """Sum the odd numbers in a list of numbers and return the result."""
    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total

print(sum_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


EJERCICIO 2-
def unique_list(numbers):
    """Return a list of unique elements from a list."""
    return list(set(numbers))

print(unique_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]))


EJERCICIO 3-
def lista_unicos_en_orden(numbers):
    lista_unicos = []
    vistos = set()

    for numero in numbers:
        if numero not in vistos:
            vistos.add(numero)
            lista_unicos.append(numero)

    return lista_unicos

# Prueba la función
print(lista_unicos_en_orden([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3]))


EJERCICIO 4-
def even_numbers(numbers):
    """Return a list of even numbers from a list of numbers."""
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens

print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


EJERCICIO 5-
def numeros_impares(numeros):
    impares = [x for x in numeros if x % 2 != 0]
    return impares

# Prueba la función
print(numeros_impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


EJERCICIO 6-
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def numeros_primos(numeros):
    primos = [x for x in numeros if es_primo(x)]
    return primos

# Prueba la función
print(numeros_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


EJERCICO 7-
def es_palindromo(numero):
    numero_str = str(numero)
    return numero_str == numero_str[::-1]

def palindromos(numeros):
    lista_palindromos = [x for x in numeros if es_palindromo(x)]
    return lista_palindromos

# Prueba la función
print(palindromos([1, 2, 3, 10, 11, 12, 13, 14, 22, 23, 33, 44, 55, 66, 77, 88, 99, 101, 111, 252, 262, 292, 300, 301]))