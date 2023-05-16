"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01
class Estudiante1:
    def __init__(self, estd):
        self.estd = estd

    def saludo(self):

        print(f"Buenas tardes, {self.estd} un gusto saludarlo")


estd = Estudiante1("Lionel Messi")
estd.saludo()

# clase 02
class Cuadrado:
    """
    Define un cuadrado según su base y su altura.
    """
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return self.b * self.h

cuadrado = Cuadrado(30, 20)
print("Área del cuadrado es igual = ", cuadrado.area(), "metros")