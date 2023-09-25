from clases.Vehiculo import Vehiculo
from clases.Bicicleta import Bicicleta
from clases.Coche import Coche
from clases.Camioneta import Camioneta
from clases.Motocicleta import Motocicleta

vehiculo = Vehiculo("verde", 0)
coche = Coche("rojo", 4, 20, 2000)
camioneta = Camioneta("marron", 4, 20, 2000, 1000)
bici = Bicicleta("azul", 2, "urbana")
moto = Motocicleta("rojo", 2, "deportiva", 180, 900)

lista = [vehiculo, coche, camioneta, bici, moto]

def catalogar(lista):
    i = 0
    for v in lista:
        if vehiculo.ruedas == i:
            print(type(v).__name__, v)
        else:
            pass
        i += 1



catalogar(lista)