

class KataSimple:
    def contar(self,cadena):
        if cadena == "":
            return 0
        else:
            numeros = cadena.split(",")
            cantidad = 0
            for caracter in numeros:
                cantidad = cantidad + 1
            return cantidad