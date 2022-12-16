import xml.etree.cElementTree as ET
import os
from Jugadores import ListaJugadores

ListadoJugadores = ListaJugadores()


class Menu:
    def __init__(self):
        try:
            print("------------Manu------------")
            print("1. Cargar el archivo XML")
            print("2. Elejir a un jugador para la simulacion")
            print("3. Simular todos los jugadores en el sistema")
            print("4. Top 10 de jugadores")
            print("5. Visualizar el estado de pila de los jugadores")
            print("6. Visualizar el estado de cola de los jugadores")
            print("7. Salir")

            seleccion =  int(input("Ingrese una opcion: "))
            
            while seleccion != 0:
                if seleccion == 1:
                    print()
                    Lectura()
                if seleccion == 2:
                    pass
                if seleccion == 3:
                    pass
                if seleccion == 4:
                    pass
                if seleccion == 5:
                    pass
                if seleccion == 6:
                    pass
                if seleccion == 7:
                    Salir()
            
        except:
            print("Error al cargar el archivo XML")
            Menu()

class Lectura:
    def __init__(self):
        try:
            print('1. Cargar archivo de jugadores')
            print('2. Cargar archivo de premios')
            
            opcion = int(input('Elija de una las opcciones: '))
            
            while opcion != 0:
                if opcion == 1:
                    print()
                    self.jugadores()
                if opcion == 2:
                    print()
                    self.premio()
        except:
            print('Ingrese un valor valido')
            Menu()
        
    def jugadores(self):
        
        ruta = input('Ingrese la ruta de su archivo: ')
        
        tree = ET.parse(ruta)
        raiz = tree.getroot()
        
        nombre = ''
        edad = 0
        movimientos = 0
        tamaño = 0
        figura = ''
        puzzle = []
        solucion = []
        
        for dato in raiz:
            for datos1 in dato:
                if datos1.tag == 'datospersonales':
                    for dato2 in datos1:
                        if dato2.tag == 'nombre':
                            print(dato2.text)
                        if dato2.tag == 'edad':
                            print(dato2.text)
                if datos1.tag == 'movimientos':
                    print(datos1.text)
                if datos1.tag == 'tamaño':
                    print(datos1.text)
                if datos1.tag == 'figura':
                    print(datos1.text)
                if datos1.tag == 'puzzle':
                    print('puzzle')
                    for dato2 in datos1:
                        print(int(dato2.attrib.get('f')),int(dato2.attrib.get('c')))
                if datos1.tag == 'solucion':
                    print('solucios')
                    for dato2 in datos1:
                        print(int(dato2.attrib.get('f')),int(dato2.attrib.get('c')))
        
    def premio(self):
        ruta = input('Ingrese la ruta de su archivo: ')
        premio = ''
        posicion = 0
        
        tree = ET.parse(ruta)
        raiz = tree.getroot()
        for dato in raiz:
            for dato2 in dato:
                if dato2.tag == 'lugar':
                    posicion = int(dato2.text)
                    print(posicion)
                if dato2.tag == 'regalo':
                    premio = dato2.text
                    print(premio)
                
            
        

class Salir():
    def __init__(self):
        
        print("Desea salir de la aplicacion")
        print("1. Sí")
        print("2. No")
        selecion = int(input())
        
        while selecion != 0:
            if selecion == 1:
                print("Regrese pronto :3")
                os._exit(0)
            if selecion == 2:
                Menu()
            else:
                print("Seleccion no valida.")
                Salir()

Menu()