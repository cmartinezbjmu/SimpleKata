

class KataSimple:
    def contar(self,cadena):
        if cadena == "":
            return 0
        else:
            cantidad = 0
            for caracter in cadena:
                cantidad = cantidad + 1
            return cantidad