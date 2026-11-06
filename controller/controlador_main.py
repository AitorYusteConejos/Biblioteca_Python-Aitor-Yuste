from model.Libro import Libro
from model.Socio import Socio
from model.DAO.dao_libros import LibroDAO
from model.DAO.dao_socios import SocioDAO
from errors.error_biblioteca import (
    SocioInexistenteError,
    SocioEnPrestamoError,
    LibroInexistenteError,
    LibroNoDisponibleError,
)

from errors.error_biblioteca import *

from view.view import menu_bilioteca, menu_libros, menu_socios

from datetime import datetime

class ControladorBiblioteca:
    def __init__(self, libros, socios, dao_libros, dao_socios):
        self.libros = libros
        self.socios = socios
        self.dao_libros = dao_libros
        self.dao_socios = dao_socios

    def iniciar(self):
        while True:
            menu_bilioteca()
            opcion = input("Elige una opcion: ").strip()

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
                    print("Opción invalida.")

    def iniciar_prestamo(self):
        try:

            codigo_socio = input("Introduce el código del socio: ").strip()
            socio_encontrado = None

            for socio in self.socios:
                if socio.codigo == codigo_socio:
                    socio_encontrado = socio
                    break

            if socio_encontrado is None:
                raise SocioInexistenteError(
                    "No existe ningún socio con ese código",
                    codigo_socio
                )

            if socio_encontrado.tiene_prestamo() == True:
                raise SocioEnPrestamoError(
                    "El socio ya tiene un libro prestado",
                    codigo_socio
                )

            print(f"Socio encontrado: {socio_encontrado.nombre}")

            titulo = input("Introduce el título o parte del título: ").strip()

            if titulo == "":
                print("Debes introducir un título.")
                return

            libros_encontrados = self.buscar_por_titulo(titulo)

            if len(libros_encontrados) == 0:
                print("No se ha encontrado ningún libro con ese título.")
                return

            print("\nLibros encontrados:")

            for libro in libros_encontrados:
                if libro.esta_dispo() == True:
                    estado = "Disponible"
                else:
                    estado = "Prestado"

                print(f"{libro.codigo} | {libro.titulo} | {estado}")

            codigo_libro = input(
                "\nIntroduce el código del libro que quieres: "
            ).strip()

            libro_elegido = None

            for libro in libros_encontrados:
                if libro.codigo == codigo_libro:
                    libro_elegido = libro
                    break

            if libro_elegido is None:
                raise LibroInexistenteError(
                    "El código no corresponde a ningún libro de la lista",
                    codigo_libro
                )

            if libro_elegido.esta_dispo() == False:
                raise LibroNoDisponibleError(
                    "El libro ya está prestado",
                    codigo_libro
                )

            libro_elegido.prestar(socio_encontrado.codigo)
            socio_encontrado.alquilar_libro(libro_elegido.codigo)

            print("Préstamo realizado correctamente.")

        except SocioInexistenteError as error:
            print(f"{error}. Código: {error.codigo}")

        except SocioEnPrestamoError as error:
            print(f"{error}. Código: {error.codigo}")

        except LibroInexistenteError as error:
            print(f"{error}. Código: {error.codigo}")

        except LibroNoDisponibleError as error:
            print(f"{error}. Código: {error.codigo}")


        libro_elegido.prestar(socio_encontrado.codigo)
        socio_encontrado.alquilar_libro(libro_elegido.codigo)

        self.registrar_evento(
            "PRÉSTAMO",
            f"Libro: {libro_elegido.codigo}; Socio: {socio_encontrado.codigo}"
        )

        print("Préstamo realizado correctamente.")


    
    def acabar(self):
        self.dao_libros.guardar_libros(self.libros)
        self.dao_socios.guardar_socios(self.socios)
        print("Datos guardados. ¡Hasta Proto!")



    def buscar_por_titulo(self, termino):
        encontrados = []

        for libro in self.libros:
            if termino.lower() in libro.titulo.lower():
                encontrados.append()

        return encontrados

    def registrar_evento(self, evento, detalles):
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("log.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"[{fecha}][{evento}][{detalles}]\n")
        