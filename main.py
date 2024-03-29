import xml.etree.cElementTree as ET
import os
import webbrowser as wb

from Jugadores import ListaJugadores
from Regalos import ListaRegalos

ListadoJugadores = ListaJugadores()

regalos = ListaRegalos()

class Menu:
    def __init__(self):
        try:
            print("-----------------Menu-----------------")
            print("1. Cargar el archivo XML")
            print("2. Simular con un jugador")
            print("3. Simular todos los jugadores en el sistema")
            print("4. Top 10 de jugadores")
            print("5. Visualizar el estado de cola de los jugadores")
            print("6. Visualizar el estado de pila de los premios")
            print("7. Salir")

            seleccion =  int(input("Ingrese una opcion: "))

            while seleccion != 0:
                if seleccion == 1:
                    print()
                    Lectura()
                if seleccion == 2:
                    print()
                    Seleccion()
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
        
        try:
            ruta = input('Ingrese la ruta de su archivo: ')
            tree = ET.parse(ruta)
            raiz = tree.getroot()
            
            nombre = ''
            edad = 0
            movimientos = 0
            tamanio = 0
            figura = ''
            jugador = None
            puntos = 0
            
            arbol = False
            estrella = False
            regalo = False
            
            for dato in raiz:
                for datos1 in dato:
                    if datos1.tag == 'datospersonales':
                        for dato2 in datos1:
                            if dato2.tag == 'nombre':
                                nombre = (dato2.text)
                            if dato2.tag == 'edad':
                                edad = int(dato2.text)
                    if datos1.tag == 'movimientos':
                        movimientos = int(datos1.text)
                        if movimientos < 5:
                            puntos = 100
                        elif movimientos > 4 and movimientos < 10:
                            puntos = 75
                        elif movimientos > 9 and movimientos < 15:
                            puntos = 50
                        elif movimientos > 14 and movimientos < 20:
                            puntos = 25
                        elif movimientos > 19 and movimientos < 10000:
                            puntos = 0
                        elif movimientos > 10000:
                            print('Moviemientos fura de rango')
                            break
                    if datos1.tag == 'tamaño':
                        tamanio = int(datos1.text)
                        if (tamanio % 5) == 0 and tamanio < 31:
                            if tamanio == 5:
                                puntos += 25
                            elif tamanio == 10:
                                puntos += 50
                            elif tamanio == 15:
                                puntos += 75
                            elif tamanio == 20:
                                puntos += 100
                            elif tamanio == 25:
                                puntos += 150
                            elif tamanio == 30:
                                puntos += 200
                        else:
                            print('Tamaño fura de rango')
                            break
                    if datos1.tag == 'figura':
                        figura = datos1.text
                        jugador = ListadoJugadores.insertarJugador(nombre,edad,movimientos,tamanio,figura,puntos)
                    if datos1.tag == 'puzzle':
                        for dato3 in datos1:
                            x = int(dato3.attrib.get('f'))
                            y = int(dato3.attrib.get('c'))
                            jugador.puzzle.insertar(jugador.id,x,y)
                    if datos1.tag == 'solucion':
                        for dato4 in datos1:
                            x = int(dato4.attrib.get('f'))
                            y = int(dato4.attrib.get('c'))
                            jugador.solucion.insertar(jugador.id,x,y)
                    
            if jugador == None:
                print('Sucedio un error en la carga de archivos.\nIntente de nuevo.')
                
                Lectura()
            elif jugador != None:
                print('Carga de archivos con exito\n')
                ListadoJugadores.graficar()
                Menu()
            
        except:
            print('Ruta ingresada no valida\nIntente de nuevo')
            Menu()

    def premio(self):
        try:
            ruta = input('Ingrese la ruta de su archivo: ')
            premio = ''
            posicion = 0
            validar = None
            tree = ET.parse(ruta)
            raiz = tree.getroot()
            for dato in raiz:
                for dato2 in dato:
                    if dato2.tag == 'lugar':
                        posicion = int(dato2.text)
                    if dato2.tag == 'regalo':
                        premio = dato2.text
                        validar = regalos.insertarRegalo(posicion,premio)
            if validar == None:
                print('Sucedio un error en la carga de archivos.\nIntente de nuevo.')
                Lectura()
            elif validar != None:
                print('Carga de archivos con exito\n')
                regalos.graficar()
                Menu()

        except:
            print('Archivo ingresado no valido\n')
            Menu()

class Salir:
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

class Seleccion:
    def __init__(self):
        try: 
            print("Se realizara la simulacion del un jugador\n")

            #jugador = ListadoJugadores.buscar(buscar)
            jugador = ListadoJugadores.cabecera()
            
            if jugador == None:
                print("No se encontro el jugador. Intente de nuevo\n")
                Menu()
            
            tamano = jugador.tamaño
            id = jugador.id
            
            jugador.puzzle.graficar(id,tamano)
            print("Puzzle del jugador: ",jugador.nombre)
            wb.open_new_tab(r'Puzzle.pdf')
            
            jugador.solucion.graficar(id,tamano)
            print("Solucion del jugador: ",jugador.nombre)
            wb.open_new_tab(r'Solucion.pdf')
            
            ListadoJugadores.eliminar()
            Menu()
            
        except:
            print("Algo salio mal, intente de nuevo\n")
            Menu()

class Top:
    def __init__(self):
        pass
Menu()