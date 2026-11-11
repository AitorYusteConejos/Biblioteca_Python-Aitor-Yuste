from datetime import datetime

from model.libro import Libro
from model.socio import Socio
from errors.error_biblioteca import ErrorBiblioteca
from view.view import View as view


class ControladorBiblioteca:

    def __init__(self, libros, socios, dao_libros, dao_socios):
        self.libros = libros
        self.socios = socios
        self.dao_libros = dao_libros
        self.dao_socios = dao_socios


    def iniciar(self):
        while True:
            view.menu_biblioteca()
            opcion = view.pedir_dato("Elige una opción: ")

            match opcion:
                case "1":
                    self.gestion_libros()

                case "2":
                    self.gestion_socios()

                case "3":
                    self.iniciar_prestamo()

                case "4":
                    self.devolver_libro()

                case "5":
                    self.acabar()
                    break

                case _:
                    view.mostrar_mensaje("Opción inválida.")

    def gestion_libros(self):
        while True:
            view.menu_libros()
            opcion = view.pedir_dato("Elige una opción: ")

            match opcion:
                case "1":
                    view.mostrar_libros(self.libros)

                case "2":
                    disponibles = []

                    for libro in self.libros:
                        if libro.esta_dispo():
                            disponibles.append(libro)

                    view.mostrar_libros(disponibles)

                case "3":
                    titulo = view.pedir_dato("Título o parte del título: ")

                    if titulo == "":
                        view.mostrar_mensaje("Debes introducir un título.")
                    else:
                        encontrados = self.buscar_por_titulo(titulo)
                        view.mostrar_libros(encontrados)

                case "4":
                    self.anadir_libro()

                case "5":
                    break

                case _:
                    view.mostrar_mensaje("Opción inválida.")

    def gestion_socios(self):
        while True:
            view.menu_socios()
            opcion = view.pedir_dato("Elige una opción: ")

            match opcion:
                case "1":
                    self.listar_prestamos()

                case "2":
                    self.anadir_socio()

                case "3":
                    break

                case _:
                    view.mostrar_mensaje("Opción inválida.")

    def buscar_por_titulo(self, termino):
        encontrados = []

        for libro in self.libros:
            if termino.lower() in libro.titulo.lower():
                encontrados.append(libro)

        return encontrados

    def buscar_libro(self, codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                return libro

        raise ErrorBiblioteca("No existe el libro", codigo)

    def buscar_socio(self, codigo):
        for socio in self.socios:
            if socio.codigo == codigo:
                return socio

        raise ErrorBiblioteca("No existe el socio", codigo)

    def anadir_libro(self):
        codigo = view.pedir_dato("Código del libro: ")

        for libro in self.libros:
            if libro.codigo == codigo:
                view.mostrar_mensaje("Ya existe un libro con ese código.")
                return

        titulo = view.pedir_dato("Título: ")
        autor = view.pedir_dato("Autor: ")
        categoria = view.pedir_dato("Categoría: ")

        if codigo == "" or titulo == "" or autor == "" or categoria == "":
            view.mostrar_mensaje("Los campos no pueden estar vacíos.")
            return

        if ";" in codigo or ";" in titulo or ";" in autor or ";" in categoria:
            view.mostrar_mensaje("Los campos no pueden contener punto y coma.")
            return

        try:
            anio = int(view.pedir_dato("Año: "))
        except ValueError:
            view.mostrar_mensaje("El año debe ser un número entero.")
            return

        libro_nuevo = Libro(codigo, titulo, autor, anio, categoria)
        self.libros.append(libro_nuevo)

        view.mostrar_mensaje("Libro añadido correctamente.")

        self.registrar_evento(
            "Libro añadido",
            f"Libro: {codigo}"
        )

    def anadir_socio(self):
        codigo = view.pedir_dato("Código del socio: ")

        for socio in self.socios:
            if socio.codigo == codigo:
                view.mostrar_mensaje("Ya existe un socio con ese código.")
                return

        nombre = view.pedir_dato("Nombre: ")
        email = view.pedir_dato("Email: ")

        if codigo == "" or nombre == "" or email == "":
            view.mostrar_mensaje("Los campos no pueden estar vacíos.")
            return

        if ";" in codigo or ";" in nombre or ";" in email:
            view.mostrar_mensaje("Los campos no pueden contener punto y coma.")
            return

        socio_nuevo = Socio(codigo, nombre, email)
        self.socios.append(socio_nuevo)

        view.mostrar_mensaje("Socio añadido correctamente.")

        self.registrar_evento(
            "Socio añdido",
            f"Socio: {codigo}")

    def iniciar_prestamo(self):
        codigo_libro = view.pedir_dato("Código del libro: ").upper()
        codigo_socio = view.pedir_dato("Código del socio: ").upper()

        try:
            libro = self.buscar_libro(codigo_libro)
            socio = self.buscar_socio(codigo_socio)

            if libro.esta_dispo() == False:
                raise ErrorBiblioteca(
                    "El libro ya está prestado",
                    codigo_libro
                )

            if socio.tiene_prestamo():
                raise ErrorBiblioteca(
                    "El socio ya tiene un préstamo",
                    codigo_socio
                )

            libro.prestar(codigo_socio)
            socio.alquilar_libro(codigo_libro)

            self.registrar_evento(
                "PRÉSTAMO",
                f"Libro: {codigo_libro}; Socio: {codigo_socio}"
            )

            view.mostrar_mensaje("Préstamo realizado correctamente.")

        except ErrorBiblioteca as error:
            view.mostrar_mensaje(f"{error}. Código: {error.codigo}")

    def devolver_libro(self):
        codigo_socio = view.pedir_dato("Código del socio: ").upper()

        try:
            socio = self.buscar_socio(codigo_socio)

            if socio.tiene_prestamo() == False:
                raise ErrorBiblioteca(
                    "El socio no tiene ningún préstamo",
                    codigo_socio
                )

            libro = self.buscar_libro(socio.cod_libro)

            if libro.cod_socio != codigo_socio:
                raise ErrorBiblioteca(
                    "Los datos del préstamo no coinciden",
                    codigo_socio
                )

            libro.devolver()
            socio.devolver()

            self.registrar_evento(
                "DEVOLUCIÓN",
                f"Libro: {libro.codigo}; Socio: {codigo_socio}"
            )

            view.mostrar_mensaje("Libro devuelto correctamente.")

        except ErrorBiblioteca as error:
            view.mostrar_mensaje(f"{error}. Código: {error.codigo}")

    def listar_prestamos(self):
        prestamos = []

        try:
            for socio in self.socios:
                if socio.tiene_prestamo():
                    libro = self.buscar_libro(socio.cod_libro)
                    prestamos.append((socio, libro))

            view.mostrar_prestamos(prestamos)

        except ErrorBiblioteca as error:
            view.mostrar_mensaje(f"{error}. Código: {error.codigo}")

    def registrar_evento(self, evento, detalles):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("log.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"[{fecha}][{evento}][{detalles}]\n")

    def acabar(self):
        self.dao_libros.guardar_libros(self.libros)
        self.dao_socios.guardar_socios(self.socios)

        view.mostrar_mensaje("Datos guardados. ¡Hasta pronto!")