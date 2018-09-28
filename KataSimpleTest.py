from unittest import TestCase

from KataSimple import KataSimple

class KataSimpleTest(TestCase):
    def test_contar(self):
        self.assertEqual(KataSimple().contar(""),0,"Cadena vacia")

    def test_contar_numero(self):
        self.assertEqual(KataSimple().contar("1"),1,"Contar un numero")

    def test_contar_tresNumeros(self):
        self.assertEqual(KataSimple().contar("1,2,3"),3,"Contar tres numeros")

