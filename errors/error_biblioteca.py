

class LibroInexistenteError(Exception):
    def __init__(self, mensaje, codigo):
        self.codigo = codigo
        super().__init__(mensaje)

class SocioInexistenteError(Exception):
    def __init__(self, mensaje, codigo):
        self.codigo = codigo
        super().__init__(mensaje)

class LibroNoDisponibleError(Exception):
    def __init__(self, mensaje, codigo):
        self.codigo = codigo
        super().__init__(mensaje)   

class SocioEnPrestamoError(Exception):
    def __init__(self, mensaje, codigo):
        self.codigo = codigo
        super().__init__(mensaje)

class SocioNoTienePrestamoError(Exception):
    def __init__(self, mensaje, codigo):
        self.codigo = codigo
        super().__init__(mensaje)  

class CodigoDuplicadoError(Exception):
    def __init__(self,mensaje, codigo):
        self.codigo = codigo
        super().__init__(mensaje)

