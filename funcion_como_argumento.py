## FUNCIONES COMO ARGUMENTOS:

# ESTAS FUNCIONES COMO ARGUMENTO SON LLAMADAS CALLBACK
def aplicar_funcion(func, valor):
    return func(valor)

def cuadrado(x):
    return x * x

def cubo(x):
    return x * x * x

print(aplicar_funcion(cuadrado, 3))
print(aplicar_funcion(cubo, 3)) 