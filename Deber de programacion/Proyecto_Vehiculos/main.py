#Desarrolla un sistema de vehículos con una clase base Vehiculo y clases derivadas Coche, Motocicleta y Camion. 
#Incluye métodos para calcular el consumo de combustible y la velocidad máxima.
from modelos.coche import Coche
print("Bienvenidos al sistema de vehiculos")
v = Coche()
print(v.consumo(), v.velocidad_maxima())
