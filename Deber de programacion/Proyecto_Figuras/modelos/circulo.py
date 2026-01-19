
import math
from modelos.figura import Figura

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcularArea(self):
        return math.pi * self.radio ** 2
