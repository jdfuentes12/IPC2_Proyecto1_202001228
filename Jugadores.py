from NodoJugadores import Jugadores
import os
import webbrowser as wb

class ListaJugadores:
    def __init__(self):
        self.heard = None
        self.size = 0
        self.id = 1
        
    def insertarJugador(self,nombre,edad, movimientos, tamanio, figura,puntos):
        Nodo_nuevo = Jugadores(self.id, nombre,edad, movimientos, tamanio, figura,puntos)
        
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

    def cabecera(self):
        tmp = self.heard
        return tmp

    def eliminar(self):
        if self.heard == None:
            print('Lista vacia')
        elif self.heard.siguiente == None:
            self.heard = None
            self.size -= 1
        else:
            tmp = self.heard
            self.heard = None
            self.heard = tmp.siguiente
            self.size -= 1
    
    def top(self):
        ultimo = None
        while ultimo != self.primero.siguiente:
            comp1 = comp2 = self.primero

            while comp2.siguiente != ultimo:
                temp = comp2.siguiente

                if comp2.puntos < temp.puntos:
                    comp2.siguiente = temp.siguiente
                    temp.siguiente=comp2

                    if comp2 != self.primero:
                        comp1.siguiente = temp
                    else:
                        self.primero = temp
                    comp2,temp = temp,comp2

                comp1 = comp2
                comp2 = comp2.siguiente
            ultimo=comp2
    
    
    def graficar(self):
        tmp = self.heard
        contador = 1
        archivo = open('ListaJugadores.dot','w',encoding='utf-8')
        
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
                archivo.write('label = "<f0>nombre: ' + tmp.nombre +'|edad: '+str(tmp.edad)+'|figura: '+tmp.figura+'|puntos: '+str(tmp.puntos)+'" \n')
                archivo.write('shape = "record"\n')
                archivo.write('fillcolor = "brown:yellow"\n')
                archivo.write('gradientangle = 100\n')
                archivo.write('];\n')
                
                if contador == 1:
                    archivo.write('"Jugadores":f1 -> "')
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
            os.system('dot -Tpdf ListaJugadores.dot -o ListaJugadores.pdf')
            wb.open_new('ListaJugadores.pdf')