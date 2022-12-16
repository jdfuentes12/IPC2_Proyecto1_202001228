from NodoJugadores import Jugadores

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
        else:
            temporal = self.heard
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = Nodo_nuevo
            self.size += 1
        return Nodo_nuevo