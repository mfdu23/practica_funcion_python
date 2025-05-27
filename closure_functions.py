def exterior(x):
    def interior(y):
        return x + y
    return interior

# Creamos una clausura llamando a la función EXTERIOR

clausura = exterior(10)

#Ahora cuando llamemos a la función clausura va a RECORDAR el valor que le dimos

resultado = clausura(5)

print(resultado)