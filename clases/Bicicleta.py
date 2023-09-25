from clases.Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        if tipo not in ["urbana", "deportiva", "montaña"]:
            raise ValueError("tipo de bicicleta no válido")
        self.tipo = tipo
    def __str__(self):
        return Vehiculo.__str__(self) + ", {}".format(self.tipo)