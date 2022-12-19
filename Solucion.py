from NodoSolucion import Solucion
import os

class ListaSolucion:
    def __init__(self):
        self.heard = None
        
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
    
    def graficar(self,id,tamano):
        archivo = open("Solucion.dot","w",encoding="utf-8")
        
        archivo.write('digraph G { \n')
        archivo.write('fontname="Helvetica,Arial,sans-serif"  \n')
        archivo.write('node [fontname="Helvetica,Arial,sans-serif"] \n')
        archivo.write('edge [fontname="Helvetica,Arial,sans-serif"]\n')
        archivo.write('a0 [shape=none  label=<\n')
        archivo.write('<TABLE border="0" cellspacing="10" cellpadding="10" >\n')
        
        tmp = self.heard
        for i in range(tamano):
            archivo.write('<TR>\n')
            for j in range(tamano):
                if tmp.id == id:
                    if tmp.siguiente is None:
                        archivo.write('<TD bgcolor="black" width="30" height="30" ></TD>\n')
                    elif tmp.x == i and tmp.y == j:
                        archivo.write('<TD bgcolor="red" width="30" height="30" ></TD>\n')
                        tmp = tmp.siguiente
                    else:
                        archivo.write('<TD bgcolor="black" width="30" height="30" ></TD>\n')
            archivo.write('</TR>\n')
        
        archivo.write('</TABLE>>]; \n')
        archivo.write('}\n')
        archivo.close()
        
        os.system('dot -Tpng Solucion.dot -o Solucion.png')