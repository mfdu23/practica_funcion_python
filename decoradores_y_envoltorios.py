# DECORADOR y WRAPPER
def decorador(function):
    def envoltorio():
        print("Esta funcionalidad se dispararía antes de la función que nos pasen por argumento")
        function()
        print("Esta funcionalidad se dispararía después de la función que nos pasen por argumento")
    return envoltorio

def saludar():
    print("Hola, estoy saludando")

saludo_decorado = decorador(saludar)

saludo_decorado()