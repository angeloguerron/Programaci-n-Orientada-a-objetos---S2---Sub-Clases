
from modelos.vehiculo import Vehiculo

class Camion(Vehiculo):
    def consumo(self):
        return "25 L/100km"

    def velocidad_maxima(self):
        return "120 km/h"
