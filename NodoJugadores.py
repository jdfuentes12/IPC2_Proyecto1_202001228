from Celdas import ListaCeldas
from Solucion import ListaSolucion

class Jugadores:
    def __init__(self, id, nombre, edad, movimientos, tamanio,figura):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.movimientos = movimientos
        self.tamaño = tamanio
        self.figura = figura
        self.puzzle = ListaCeldas()
        self.solucion = ListaSolucion()
        self.siguiente = None