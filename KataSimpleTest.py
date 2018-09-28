from unittest import TestCase

from KataSimple import KataSimple

class KataSimpleTest(TestCase):
    def test_calcular(self):
        self.assertEqual(KataSimple().calcular(""),0,"Cadena vacia")
