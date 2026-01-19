
from personajes.personaje import Personaje

class Guerrero(Personaje):
    def atacar(self):
        return "Espada"

    def defender(self):
        return "Escudo"
