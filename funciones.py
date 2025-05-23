# def saludar(nombre, apellido = "Dupraz"):
#     print("Hola", nombre, apellido)

# saludar("Martín")

# def saludar(*nombres): # De esta forma si no se la cantidad de argumentos que voy a pasar
#     if len(nombres) > 1:
#         print("Hola", nombres[0], nombres[1]) 
#     else:
#         print("Hola", nombres[0]) 

# saludar("Martín", "Dupraz")

# def padre_orgulloso(nene1, nene2, nene3):
#     print("Mis hijos son:", nene1, nene2, nene3)
#     print("Y el mas pequeño es", nene3)

# padre_orgulloso(nene1 = "Ricardito", nene2 = "Nicolas", nene3 = "Juancito") # Si no especifico los keywords argument los argumentos pasan desordenados

# def padre_orgulloso(**nenes): #Esto si nos sabemos la cantidad de argumentos que vamos a recibir y los necesitamos de forma ordenada
#     print("Mis hijos son:", nenes["a"], nenes["b"], nenes["c"])
#     print("Y el mas pequeño es", nenes["c"])

# padre_orgulloso(a = "Ricardito", b = "Nicolas", c = "Juancito") # Si no especifico los keywords argument los argumentos pasan desordenados

# def mostrar_mercaderia(mercaderia):
#     for item in mercaderia:
#         print(item)

# lista_frutas = ["Manzana", "Perá", "Platano"]

# mostrar_mercaderia(lista_frutas)

# def suma(a, b):
#     resultado = a + b # variable local
#     return resultado

# resultado = suma(2,3) # Resultado variable global

# print(resultado)

# def suma(a, b):
#     """resultado = a + b # variable local
#     return resultado"""
#     pass # si no tengo la definición de la función pongo pass para que no tire error

# resultado = suma(2,3) # Resultado variable global

# print(resultado)

# def devolver_cuadrado(x):
#     """Devuelve el cuadrado del argumento pasado por parámetro"""
#     return x**2

# print(devolver_cuadrado(x = 2))

# def devolver_cuadrado(x, /): # De esta forma me obliga a no mandar keyword argument
#     """Devuelve el cuadrado del argumento pasado por parámetro"""
#     return x**2

# print(devolver_cuadrado(x = 2))

# def devolver_cuadrado(*, x): # De esta forma me obliga a no mandar posicional argument
#     """Devuelve el cuadrado del argumento pasado por parámetro"""
#     return x**2

# print(devolver_cuadrado(2))

# def calcular_resultado(a, b, /, *, c, d): # En este caso va a esperar a y b como posicional arguments y a c y d como keyboard argument
#     print(a + b +c+ d)

# calcular_resultado(1, 2, c = 3, d = 4)

def operaciones(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division) # Devolvemos tupla para que no se manipule el resultado de la función

print(operaciones(4,2))