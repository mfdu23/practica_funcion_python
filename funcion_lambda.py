# FUNCIONES LAMBDA

# # Función tradicional
# def duplicar(num):
#     return num * 2

# print(duplicar(5))

# --------------------------------------

# # Función lambda
# duplicar_lambda = lambda num: num * 2
# print(duplicar_lambda(5))

# mupltiplicar_lambda = lambda a,b: a * b
# print(mupltiplicar_lambda(5,4))

# cuadrado_lambda = lambda num: num * num
# print(cuadrado_lambda(3))

# --------------------------------------

# def operaciones(operacion):
#     if operacion == "suma":
#         return lambda x,y: x + y
#     elif operacion == "resta":
#         return lambda x,y: x - y
#     elif operacion == "multiplicacion":
#         return lambda x,y: x * y
#     else:
#         return lambda x,y: x / y
    
# suma = operaciones("suma")

# print(suma(10,5))

# --------------------------------------

# def multiplicador(n):
#     return lambda x: x * n

# triplicar = multiplicador(3)

# print(triplicar(5))

# --------------------------------------

# estudiantes = [
#     {"nombre": "Juan", "edad": 20},
#     {"nombre": "María", "edad": 25},
#     {"nombre": "Pedro", "edad": 22}
# ]

# estudiantes_ordenados = sorted(estudiantes, key = lambda x: x['edad'])
# print(estudiantes_ordenados)