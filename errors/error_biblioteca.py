class ErrorBiblioteca(Exception):
    def __init__(self, mensaje, codigo):
        self.codigo = codigo
        super().__init__(mensaje)