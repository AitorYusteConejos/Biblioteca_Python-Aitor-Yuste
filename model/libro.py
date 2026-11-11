class Libro:
    def __init__(self, codigo, titulo, autor, anio, categoria, cod_socio=None):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.categoria = categoria
        self.cod_socio = cod_socio

    def __str__(self):
        return (
            f"Libro(codigo={self.codigo}, titulo={self.titulo}, "
            f"autor={self.autor}, anio={self.anio}, "
            f"categoria={self.categoria}, cod_socio={self.cod_socio})"
        )

    def esta_dispo(self):
        return self.cod_socio is None

    def prestar(self, cod_socio):
        self.cod_socio = cod_socio

    def devolver(self):
        self.cod_socio = None
