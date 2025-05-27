# MAP: toma una función y un iterable como argumentos y aplica la función a cada elemento

# def cuadrado(x):
#     return x * x

# numeros = [1, 2, 3, 4, 5]

# cuadrados = list(map(cuadrado, numeros))

# print(cuadrados)

# FILTER: toma una función que devuelve True o False y un iterable y devuelve solo los elementos que devuelven tru como argumento de la función


# numeros = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12]

# def es_par(x):
#     return x % 2 == 0

# pares = list(filter(es_par, numeros))

# print(pares)


# REDUCE: Toma una función que  reciba dos argumentos y un iterable y aplica la función acumulativa a los elementos del iterable

# numeros = [1, 2, 3, 4, 5]

# from functools import reduce

# def suma(x, y):
#     return x + y

# sumatoria = reduce(suma, numeros)

# print(sumatoria)

# APLICANDO LAMBDA

numeros = [1, 2, 3, 4, 5]

cuadrados = list(map(lambda x: x * x, numeros))

print(cuadrados)

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)