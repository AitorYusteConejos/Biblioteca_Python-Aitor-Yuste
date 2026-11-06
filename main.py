from model.DAO.dao_socios import SocioDAO
from model.DAO.dao_libros import LibroDAO
from controller.controlador_main import ControladorBiblioteca


def main():
    dao_libros = LibroDAO()
    dao_socios = SocioDAO()

    libros = dao_libros.cargar_libros()
    socios = dao_socios.cargar_socios()

    print("Se han cargado {len(libros)} libros correctamente")
    print("Se han cargado {len(socios)} socios correctamente")

    controlador = ControladorBiblioteca(libros, socios, dao_libros, dao_socios)
    controlador.iniciar