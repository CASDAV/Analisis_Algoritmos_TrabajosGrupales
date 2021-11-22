import tablero as t
import numpy as np
import time


matriz = t.generarMatriz()


gano = False


def buscarZero(m):
    for i in range(0, 4):
        for j in range(0, 4):
            if m[i][j] == 0:
                return i, j


def buscarPos(i):
    if i < 4:
        return 0, i % 4
    if i >= 4 and i < 8:
        return 1, i % 4
    if i >= 8 and i < 12:
        return 2, i % 4
    if i >= 12 and i < 16:
        return 3, i % 4


def buscarUbi(m, buscar):
    for i in range(0, 4):
        for j in range(0, 4):
            if m[i][j] == buscar:
                return i, j


def distancia(d, h):
    x = 0
    y = 0
    if d[0] > h[0]:
        x = abs(d[0]-h[0]) * -1
    if d[1] > h[1]:
        y = abs(d[1]-h[1]) * -1
    if d[1] < h[1]:
        y = abs(d[1]-h[1])
    if d[0] < h[0]:
        x = abs(d[0]-h[0])

    return x, y

def mover(m,d):
    # primero se mueve 
    
    if abs(d[1]) != 0:
        for i in range(0,abs(d[1])):
            if d[1] >0: # hacia la derecha
                m = t.mover("d",m)
                t.imprimir(matriz)
            if d[1] < 0: # hacia la izquierda
                m = t.mover("a",m)
                t.imprimir(matriz)
    if abs(d[0]) != 0:
        for i in range(0,abs(d[0])):
            if d[0] > 0: # hacia abajo
                m = t.mover("s",m)
                t.imprimir(matriz)
            if d[0] < 0: # hacia arriba
                m = t.mover("w",m)
                t.imprimir(matriz)
    return m


# desde = buscarZero(matriz)
# hacia = buscarUbi(matriz,15)
# ds = distancia(desde,hacia)
# matriz = mover(matriz,ds)
# print( buscarZero(matriz))
# print(buscarPos(6))
# print(buscarPos(4))
# a = buscarUbi(matriz,15)
# print(a)
# print(a[0])
# print(a[1])
# print(a[0]*-1)
# print(a[1]*-1)
# print(buscarUbi(matriz,15))
# print(buscarUbi(matriz,10))
# print(buscarUbi(matriz,4))

while gano == False:
    for i in range(1, 16):
        posZero = buscarZero(matriz)
        posUbicar = buscarPos(i) #posible cambiar a --
        posNumero = buscarUbi(matriz, i)
        rvs = (posNumero[0] *-1,posNumero[1] *-1)
        # sacar pos de
        # 1) posicion actual de i
        # 2) posicion del numero a ubicar
        # 3) posicion del 0
        matriz = mover(matriz,distancia(posZero,posUbicar))
        a = (0,0)
        posNumero = buscarUbi(matriz, i)

        
        
        t.imprimir(matriz)
        time.sleep(10)
        rvs = (posNumero[0] *-1,posNumero[1] *-1)
        while(buscarPos(i) != buscarUbi(matriz, i) ) :
            #posNumero = buscarUbi(matriz, i)
            posZero = buscarZero(matriz)
            
            
            matriz = mover(matriz,distancia(posZero,posNumero))
            matriz = mover(matriz,distancia(posZero,rvs))
            
           
            time.sleep(10)
        print("-----------------------------------------------------------------------------------------------------------")
        
    
    t.imprimir(matriz)
    opcion = input("ingrese su movimiento (w,a,s,d) \n")
    matriz = t.mover(opcion, matriz)
    gano = t.verificar(matriz)

print(matriz)
print("ganaste!")
