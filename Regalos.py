from NodoRegalos import Regalos
import os
import webbrowser as wb

class ListaRegalos:
    def __init__(self):
        self.heard = None

    def insertarRegalo(self,lugar,premio):
        Nodo_nuevo = Regalos(lugar,premio)

        if self.heard is None:
            self.heard = Nodo_nuevo
        else:
            Nodo_nuevo.siguiente = self.heard
            self.heard = Nodo_nuevo
        return Nodo_nuevo 

    def graficar(self):
        tmp = self.heard
        contador = 1
        archivo = open('Regalos.dot','w',encoding='utf-8')
        
        if self.heard == None:
            print('Lista vacia')
            archivo.write('digraph G {\n')
            archivo.write('fontname="Helvetica,Arial,sans-serif"\n')
            archivo.write('\n')
            archivo.write('graph [\n')
            archivo.write('rankdir = "LR"\n')
            archivo.write('bgcolor = "white:lightblue"\n')
            archivo.write('style="filled"\n')
            archivo.write('gradientangle = 270];\n')
            archivo.write('\n')
            archivo.write('"Lista Vacia":f0 [\n')
            archivo.write('];\n')
            archivo.write('\n')
        
        elif self.heard != None:
            
            archivo.write('digraph G {\n')
            archivo.write('fontname="Helvetica,Arial,sans-serif"\n')
            archivo.write('graph [\n')
            archivo.write('rankdir = "LR"\n')
            archivo.write('bgcolor = "white:lightblue"\n')
            archivo.write('style="filled"\n')
            archivo.write('gradientangle = 270];\n')
            
            while tmp is not None:
                archivo.write('\n')
                archivo.write('"'+str(contador)+'"[\n')
                archivo.write('label = "<f0>' + str(tmp.lugar) +'|'+str(tmp.premio)+'" \n')
                archivo.write('shape = "record"\n')
                archivo.write('fillcolor = "brown:yellow"\n')
                archivo.write('gradientangle = 100\n')
                archivo.write('];\n')
                
                if contador == 1:
                    archivo.write('"Premios":f1 -> "')
                    archivo.write(str(contador))
                    archivo.write('":f0 [\n')
                    archivo.write('];\n')
                else:
                    archivo.write('"'+str(contador-1)+'":f1 -> "')
                    archivo.write(str(contador))
                    archivo.write('":f0 [\n')
                    archivo.write('];\n')
                tmp = tmp.siguiente
                contador += 1
            
            archivo.write('}\n')
            archivo.close()
            os.system('dot -Tpdf Regalos.dot -o Regalos.pdf')
            wb.open_new(r'Regalos.pdf')