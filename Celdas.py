from NodoCelda import Celdas

class ListaCeldas:
    def __init__(self,id,x,y):
        self.heard = 0
        
    def insertar(self,id,x,y):
        nuevo_Nodo = Celdas(id,x,y)
        
        if self.heard is None:
            self.heard = nuevo_Nodo
        else:
            temporal = self.heard
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nuevo_Nodo
        return nuevo_Nodo