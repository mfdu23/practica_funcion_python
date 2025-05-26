# def suma_naturales(n):
#     if n == 1:
#         return 1
#     else:
#         return n + suma_naturales(n-1)

# print(suma_naturales(5))

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))

# def contador(n):
#     print(n)
#     n += 1
#     if n < 10:
#         contador(n)

# print(contador(1))

#----------------------------
# DOCUMENTACION DE FUNCIONAES
#----------------------------

def suma(a,b):
    """Esta función suma dos números y devuelve el resultado
    Args:
        a (int): El primer número a sumar
        b (int): El segundo número a sumar
    
    Returns:
        int: La suma de los dos números
    """
    return a + b

print(suma.__doc__)