from model.socio import Socio


class SocioDAO:
    def cargar_socios(self):
        socios = []

        with open("data/Socios.txt", "r", encoding="utf-8") as archivo_socios:
            next(archivo_socios)

            for linea in archivo_socios:
                socio = linea.strip().split(";")

                codigo = socio[0]
                nombre = socio[1]
                email = socio[2]

                cod_libro = socio[3] if socio[3] else None

                socio = Socio(codigo, nombre, email, cod_libro)
                socios.append(socio)

        return socios

    def guardar_socios(self, socios):
        with open("data/Socios.txt", "w", encoding="utf-8") as archivo_socio:
            archivo_socio.write("codigo;nombre;email;cod_libro\n")

            for socio in socios:
                if socio.cod_libro is None:
                    cod_libro = ""
                else:
                    cod_libro = socio.cod_libro

                linea = f"{socio.codigo};{socio.nombre};{socio.email};{cod_libro}\n"
                archivo_socio.write(linea)