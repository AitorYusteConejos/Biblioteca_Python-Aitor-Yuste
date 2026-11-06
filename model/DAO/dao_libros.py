from model.Libro import Libro

class LibroDAO:
    def cargar_libros(self):
        libros = []

        with open("data/Libros.txt", "r", encoding="utf-8") as archivoLibros:
            next(archivoLibros)

            for linea in archivoLibros:
                libro = linea.strip().split(";")

                codigo = libro[0]
                titulo = libro[1]
                autor = libro[2]
                anio = int(libro[3])
                categoria = libro[4]

                cod_socio = libro[5] if libro[5] else None

                libro = Libro(codigo, titulo, autor, anio, categoria, cod_socio)
                libros.append(libro)

        return libros

    def guardar_libros(self, libros):
        with open("data/Libros.txt", "w", encoding="utf-8") as archivoLibro:
            archivoLibro.write("codigo;titulo;autor;anio;categoria;cod_socio\n")

            for libro in libros:
                if libro.cod_socio is None:
                    cod_socio = ""
                else:
                    cod_socio = libro.cod_socio

                linea=(f"{libro.codigo};{libro.titulo};{libro.autor};"
                       f"{libro.anio};{libro.categoria};{cod_socio}\n"
                    )
                archivoLibro.write(linea)