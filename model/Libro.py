class Libro:
    def __init__(self, codigo, titulo, autor, anio, categoria, cod_socio=None):
            self.codigo = codigo
            self.titulo = titulo
            self.autor = autor
            self.anio = anio
            self.categoria = categoria
            self.cod_socio = cod_socio

    def esta_dispo(self):
          return self.cod_socio is None

    def prestar(self, cod_socio):
          self.cod_socio = cod_socio

    def devolver(self):
          self.cod_socio = None