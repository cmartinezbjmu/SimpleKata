from unittest import TestCase
import Estadistica

class EstadisticaTest(TestCase):
    def test_calcular(self):
        self.assertEqual(Estadistica().calcular(""),0,"Cadena vacia")
