class rectangulo:
    def __init__(self, base, altura):
        self.nombre = "Rectangulo"
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura

class circulo:
    def __init__(self, radio):
        self.nombre = "Circulo"
        self.radio = radio
    def area(self):
        return 3.14159 * self.radio * self.radio

figura_1 = rectangulo(4, 3)
figura_2 = rectangulo(5, 2)
figura_3 = circulo(2)

figuras = [figura_1, figura_2, figura_3]

for figura in figuras:
    print(figura.nombre, figura.area())