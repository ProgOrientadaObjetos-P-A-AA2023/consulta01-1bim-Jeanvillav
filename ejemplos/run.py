"""

"""
# Crear dos objetos de la clase 01
class Estudiante1:
# objeto 01

    def __init__(self, nombre, c):
        self.nombre = nombre
        self.calificacion = c

    def __str__(self):
        return f"Estudiante: {self.nombre}, \nCalificacion: {self.calificacion}"


# crear
estudiante = Estudiante1("Paolo Ladino", 9.5)
# Presentar objeto; usar el método __st__
print(estudiante)
# objeto 02


# crear ingresando valores por teclado

nombre = input("Ingresa el nombre del segundo estudiante: ")
calificacion = int(input("Ingresa la calificacion obtenida: "))
persona2 = Estudiante1(nombre, calificacion)

# Presentar objeto; usar el método __st__
print(persona2)

