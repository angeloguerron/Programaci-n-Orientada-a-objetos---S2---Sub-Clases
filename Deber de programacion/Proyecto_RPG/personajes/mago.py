
from personajes.personaje import Personaje

class Mago(Personaje):
    def atacar(self):
        return "Hechizo"

    def defender(self):
        return "Magia"
