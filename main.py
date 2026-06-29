from libro import Libro
from cliente import Cliente
from biblioteca import Biblioteca

biblioteca = Biblioteca()

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
biblioteca.agregar_libro(libro1)
cliente = Cliente("Carlos Ortiz", "123456")
biblioteca.mostrar_libros()
cliente.solicitar_libro(libro1)
biblioteca.mostrar_libros()
cliente.devolver_libro(libro1)
biblioteca.mostrar_libros()