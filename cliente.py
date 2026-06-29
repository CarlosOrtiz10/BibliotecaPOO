class Cliente:
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento

    def solicitar_libro(self, libro):
        libro.prestar()

    def devolver_libro(self, libro):
        libro.devolver()