from NodoSolucion import Solucion

class ListaSolucion:
    def __init__(self,id,x,y):
        self.heard = 0
        
    def insertar(self,id,x,y):
        nuevo_Nodo = Solucion(id,x,y)
        
        if self.heard is None:
            self.heard = nuevo_Nodo
        else:
            temporal = self.heard
            while temporal.siguiente is not None:
                temporal = temporal.siguiente
            temporal.siguiente = nuevo_Nodo
        return nuevo_Nodo