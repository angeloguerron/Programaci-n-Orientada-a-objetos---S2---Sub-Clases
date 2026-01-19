#Crea una clase base Figura con un método calcularArea(). 
#Luego, crea clases derivadas Rectangulo y Circulo que implementen el método calcularArea() de manera apropiada.
from modelos.rectangulo import Rectangulo
from modelos.circulo import Circulo
print("Bienvenido base de figuras con un metodo calculador")
print("Área Rectángulo:", Rectangulo(4,5).calcularArea())
print("Área Círculo:", Circulo(3).calcularArea())
