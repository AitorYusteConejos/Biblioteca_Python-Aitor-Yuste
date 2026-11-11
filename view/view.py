
class View:
    def menu_biblioteca():
        print("\n=== MENÚ BIBLIOTECA ===")
        print("1. Gestión de libros")
        print("2. Gestión de socios")
        print("3. Iniciar préstamo")
        print("4. Devolver libro")
        print("5. Acabar")


    def menu_libros():
        print("\n=== MENÚ LIBROS ===")
        print("1. Listar todos los libros")
        print("2. Listar libros disponibles")
        print("3. Buscar libro por título")
        print("4. Añadir libro")
        print("5. Volver al menú principal")


    def menu_socios():
        print("\n=== MENÚ SOCIOS ===")
        print("1. Listar socios con préstamo")
        print("2. Añadir socio")
        print("3. Volver al menú principal")


    def pedir_dato(mensaje):
        return input(mensaje).strip()


    def mostrar_mensaje(mensaje):
        print(mensaje)


    def mostrar_libros(libros):
        if len(libros) == 0:
            print("No se han encontrado libros.")
            return

        for libro in libros:
            if libro.esta_dispo():
                estado = "Disponible"
            else:
                estado = "Prestado"

            print(
                f"{libro.codigo} | {libro.titulo} | "
                f"{libro.autor} | {libro.anio} | {estado}"
            )


    def mostrar_prestamos(prestamos):
        if len(prestamos) == 0:
            print("No hay socios con préstamos.")
            return

        for socio, libro in prestamos:
            print(
                f"{socio.codigo} | {socio.nombre} | "
                f"{libro.codigo} | {libro.titulo}"
            )