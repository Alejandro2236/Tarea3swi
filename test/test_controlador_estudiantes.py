import os.path
from unittest import TestCase

from estudiantes.controlador_estudiantes import ControladorEstudiantes


class TestControladorEstudiantes(TestCase):
    def test_cargar_archivo_valido(self):
        controlador = ControladorEstudiantes()
        realizado: bool = controlador.cargar_estudiantes_desde_csv(os.path.abspath("../data/estudiantes.csv"))
        self.assertTrue(realizado)

    def test_cargar_archivo_inexistente(self):
        controlador = ControladorEstudiantes()
        realizado = controlador.cargar_estudiantes_desde_csv("data/xyz")
        self.assertFalse(realizado)
