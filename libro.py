class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"{self.titulo} prestado.")
        else:
            print("Libro no disponible.")

    def devolver(self):
        self.disponible = True
        print(f"{self.titulo} devuelto.")