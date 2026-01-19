
class Item:
    def __init__(self, titulo):
        self.titulo = titulo
        self.prestado = False

    def prestar(self):
        self.prestado = True
        print(self.titulo, "prestado")

    def devolver(self):
        self.prestado = False
        print(self.titulo, "devuelto")
