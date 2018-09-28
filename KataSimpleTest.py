from unittest import TestCase

from KataSimple import KataSimple

class KataSimpleTest(TestCase):
    def test_contar(self):
        self.assertEqual(KataSimple().contar(""),[0,0,0,0],"Cadena vacia")

    def test_contar_numero(self):
        self.assertEqual(KataSimple().contar("1"),[1,1,0,0],"Contar un numero")

    def test_contar_tresNumeros(self):
        self.assertEqual(KataSimple().contar("1,2,3"),[3,1,0,0],"Contar tres numeros")

    def test_contar_N_Numeros(self):
        self.assertEqual(KataSimple().contar("1,2:3,4:6,7,8,9"),[8,1,0,0], "Contar con diferentes separadores")

    def test_contar_N_Numeros_retornarArreglo(self):
        self.assertEqual(KataSimple().contar("1,2:3,4:6,7,8,9"),[8,1,0,0], "Contar numeros y retornar un arreglo con la cantidad")

    def test_cantNum_Menor(self):
        self.assertEqual(KataSimple().contar("1,2:3,4:6,7,8,9"),[8,1,0,0], "Contar numeros y calcular el menor")


