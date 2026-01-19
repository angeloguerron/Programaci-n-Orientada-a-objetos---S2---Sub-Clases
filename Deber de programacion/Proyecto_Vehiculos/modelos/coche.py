
from modelos.vehiculo import Vehiculo

class Coche(Vehiculo):
    def consumo(self):
        return "8 L/100km"

    def velocidad_maxima(self):
        return "180 km/h"
