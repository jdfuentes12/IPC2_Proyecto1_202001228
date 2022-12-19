from NodoJugadores import Jugadores
from Celdas import ListaCeldas
from Solucion import ListaSolucion

class ListaJugadores:
    def __init__(self):
        self.heard = None
        self.size = 0
        self.id = 1
        
    def insertarJugador(self,nombre,edad, movimientos, tamanio, figura):
        Nodo_nuevo = Jugadores(self.id, nombre,edad, movimientos, tamanio, figura)
        
        if self.heard is None:
            self.heard = Nodo_nuevo
            self.size += 1 
            self.id += 1 
        else:
            temporal = self.heard
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = Nodo_nuevo
            self.size += 1
            self.id += 1 
        return Nodo_nuevo

    def buscar(self, nombre):
        tmp = self.heard
        validar = False
        while tmp is not None:
            if tmp.nombre == nombre:
                valdiar = True
                return tmp
            tmp = tmp.siguiente
        if validar == False:
            return None