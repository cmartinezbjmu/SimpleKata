from numpy import *

class KataSimple:
    def contar(self,cadena):
        if cadena == "":
            return [0,0,0,0]
        else:
            cadena = cadena.replace(":",",")
            numeros = cadena.split(",")
            cantidad = 0
            menor = numeros[0]
            for caracter in numeros:
                cantidad = cantidad + 1
                if caracter < menor:
                    menor = caracter
            arreglo = [cantidad,int(menor),0,0]
            return arreglo