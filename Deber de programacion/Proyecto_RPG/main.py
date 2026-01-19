#Crea una jerarquía de clases para un juego de rol. 
#Comienza con una clase base Personaje y deriva clases como Guerrero, Mago y Arquero. 
#Implementa métodos para atacar y defender con comportamientos específicos para cada clase.
from personajes.guerrero import Guerrero
print("Bievenido al juego de rol")
g = Guerrero()
print(g.atacar(), g.defender())
