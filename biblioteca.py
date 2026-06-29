class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        for libro in self.libros:
            estado = "Disponible" if libro.disponible else "Prestado"
            print(libro.titulo, "-", estado)