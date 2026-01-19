
from personajes.personaje import Personaje

class Arquero(Personaje):
    def atacar(self):
        return "Flecha"

    def defender(self):
        return "Esquivar"
