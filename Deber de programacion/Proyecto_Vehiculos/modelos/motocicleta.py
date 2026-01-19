
from modelos.vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def consumo(self):
        return "4 L/100km"

    def velocidad_maxima(self):
        return "160 km/h"
