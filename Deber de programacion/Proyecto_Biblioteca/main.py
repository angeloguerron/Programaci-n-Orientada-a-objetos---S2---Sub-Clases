#Diseña una jerarquía de clases para un sistema de biblioteca. 
#Comienza con una clase base Item y crea clases derivadas para Libro, Revista y DVD. 
#Incluye métodos para préstamo y devolución.
from items.libro import Libro
print("Bienvenido al sistema de Biblioteca")
print("Se basa en metodos de prestamos y devolución")
l = Libro("Python")
l.prestar()
l.devolver()
