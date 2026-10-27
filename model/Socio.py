class Socio:
    def __init__(self, codigo, nombre, email, cod_libro=None):
        self.codigo = codigo
        self.nombre = nombre
        self.email = email
        self.cod_libro = cod_libro

    def alquilar_libro(self, cod_libro):
        self.cod_libro = cod_libro

    def devolver(self):
        self.cod_libro = None