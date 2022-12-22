from Celdas import ListaCeldas
from Solucion import ListaSolucion
from MatrizDis_puzzle import MatrizDispersa

class Jugadores:
    def __init__(self, id, nombre, edad, movimientos, tamanio,figura,puntos):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.movimientos = movimientos
        self.tamaño = tamanio
        self.figura = figura
        #self.puzzle = MatrizDispersa(0)
        self.puzzle = ListaCeldas()
        self.solucion = ListaSolucion()
        self.puntos = puntos
        self.siguiente = None