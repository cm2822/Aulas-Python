import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def get_raio(self):
        return self.raio
    
    def set_raio(self, raio):
        if raio < 0:
            print("O raio não pode ser negativo. Insira novamente.")
    
    def calcular_area(self):
        return math.pi * self.raio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.raio
    
raio = float(input("Insira o raio do circulo --> "))
circulo = Circulo(raio)
print(circulo.get_raio())
print({circulo.calcular_area()})
print({circulo.calcular_perimetro()})