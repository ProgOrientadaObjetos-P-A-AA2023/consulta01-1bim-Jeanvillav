"""

"""
# Crear dos objetos de la clase 02
class Vehiculo:
# objeto 01

    def __init__(self, auto, m):
        self.auto = auto
        self.modelo = m

    def __str__(self):
        return f"Auto: {self.auto}, \nModelo: {self.modelo}"


# crear
auto1 = Vehiculo("Chevrolet", "Camaro")
# Presentar objeto; usar el método __st__
print(auto1)
# objeto 02


# crear ingresando valores por teclado

auto = input("Ingresa la marca del segundo auto: ")
modelo = input("Ingresa el modelo del segundo auto: ")
auto2 = Vehiculo(auto, modelo)

# Presentar objeto; usar el método __st__
print(auto2)

