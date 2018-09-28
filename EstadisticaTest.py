from unittest import TestCase

from Estadistica import Estadistica

class EstadisticaTest(TestCase):
    def test_calcular(self):
        self.assertEqual(Estadistica().calcular(""),0,"Cadena vacia")

    def test_calcular_unacadena(self):
        self.assertEqual(Estadistica().calcular("1"),1,"Un numero")

    def test_calcular_cadenaConUnNumero(self):
        self.assertEqual(Estadistica().calcular("1"),1,"Un numero")
        self.assertEqual(Estadistica().calcular("2"),2,"Un numero")
