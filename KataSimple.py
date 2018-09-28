from numpy import *

class KataSimple:
    def contar(self,cadena):
        if cadena == "":
            return [0]
        else:
            cadena = cadena.replace(":",",")
            numeros = cadena.split(",")
            cantidad = 0
            for caracter in numeros:
                cantidad = cantidad + 1
            arreglo = array([cantidad])
            return arreglo