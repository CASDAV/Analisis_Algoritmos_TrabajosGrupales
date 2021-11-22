import random
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


def mover(m, d):
    # primero se mueve

    if abs(d[1]) != 0:
        for i in range(0, abs(d[1])):
            if d[1] > 0:  # hacia la derecha
                m = t.mover("d", m)
                #t.imprimir(matriz)
            if d[1] < 0:  # hacia la izquierda
                m = t.mover("a", m)
                #t.imprimir(matriz)
    if abs(d[0]) != 0:
        for i in range(0, abs(d[0])):
            if d[0] > 0:  # hacia abajo
                m = t.mover("s", m)
                #t.imprimir(matriz)
            if d[0] < 0:  # hacia arriba
                m = t.mover("w", m)
                #t.imprimir(matriz)
    return m

def puntaje(m):
    puntaje = 0
    cont = 1
    for i in range(0, 3):
        for j in range(0, 4):
            if matriz[i][j] == cont:
                cont += 1
                puntaje += 1
            else:
                cont +=1
    if m[3][0] == 13:
        puntaje += 1
    if m[3][1] == 14:
        puntaje += 1
    if m[3][2] == 15:
        puntaje += 1
    
        
    return puntaje
                

def mejorJugada(m):
    mayor = []  # W A S D
    
    # primero miro si es mejor hacia arriba W
    m = t.mover("w", m)
    mayor.append(puntaje(m))
    m = t.mover("s", m)

    # A
    m = t.mover("a", m)
    mayor.append(puntaje(m))
    m = t.mover("d", m)
    # S
    m = t.mover("s", m)
    mayor.append(puntaje(m))
    m = t.mover("w", m)
    # D
    m = t.mover("d", m)
    mayor.append(puntaje(m))
    m = t.mover("a", m)
    
    n = 0
    pos = 0
    for i in range(0,len(mayor)):
        if mayor[i] > n:
            n = mayor[i]
            pos = i
    #print(mayor[pos])
    return pos , n


def mejorJugada2(m):
    # W A S D
    # dir, puntaje
    mejor = (-1, puntaje(m))


    # primero miro si es mejor hacia arriba W
    posZero = buscarZero(m)
    m = t.mover("w", m)
    posZero2 = buscarZero(m)
    j = puntaje(m)
    if posZero2[0] != posZero[0] or posZero[1] != posZero2[1]:
        m = t.mover("s", m)

    if j > mejor[1]:
        mejor = (0,j)

    # A
    posZero = buscarZero(m)
    m = t.mover("a", m)
    posZero2 = buscarZero(m)
    j = puntaje(m)
    if posZero2[0] != posZero[0] or posZero[1] != posZero2[1]:
        m = t.mover("d", m)
    if j > mejor[1]:
        mejor = (1,j)


    # S
    posZero = buscarZero(m)
    m = t.mover("s", m)
    posZero2 = buscarZero(m)
    j = puntaje(m)
    if posZero2[0] != posZero[0] or posZero[1] != posZero2[1]:
        m = t.mover("w", m)
    if j > mejor[1]:
        mejor = (2,j)


    # D
    posZero = buscarZero(m)
    m = t.mover("d", m)
    posZero2 = buscarZero(m)
    j = puntaje(m)
    if posZero2[0] != posZero[0] or posZero[1] != posZero2[1]:
        m = t.mover("a", m)
    if j > mejor[1]:
        mejor = (3,j)
    
    
    return mejor

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
print(puntaje(matriz))
max2 = 0
iter = 0
while iter < 50000 :
    iter += 1
    if puntaje(matriz) > max2:
        max2 = puntaje(matriz)
        mmm = matriz
    print("iteracion: " + str(iter))
    print("MAX: " + str(max2) + "ACTUAL " + str( puntaje(matriz)))
    print()
    #print("Gane?: " + str(gano))
    if(iter % 500 == 0):
        posz = buscarZero(matriz)
        xx = random.randrange(0,4,1)
        yy = random.randrange(0,4,1)
        ds = distancia(posz,(0,0))
        matriz = mover(matriz,ds)
    if(iter % 500 == 250):
        posz = buscarZero(matriz)
        xx = random.randrange(0,4,1)
        yy = random.randrange(0,4,1)
        ds = distancia(posz,(3,3))
        matriz = mover(matriz,ds)
    
    if(iter % 500 == 400):
        posz = buscarZero(matriz)
        xx = random.randrange(0,4,1)
        yy = random.randrange(0,4,1)
        ds = distancia(posz,(xx,yy))
        matriz = mover(matriz,ds)

    #---------

    # op1 = mejorJugada2(t.mover("w",matriz))

    # op2 = mejorJugada2(t.mover("a",matriz))

    # op3 = mejorJugada2(t.mover("s",matriz))

    # op4 = mejorJugada2(t.mover("d",matriz))

    # jugadas = []
    # jugadas.append(op1)
    # jugadas.append(op2)
    # jugadas.append(op3)
    # jugadas.append(op4)

    # jugada = max(jugadas)

    #---------
    jug = mejorJugada2(matriz)

    if jug[0] == -1:
        jug = (random.randrange(0,4,1),0)

    if jug[0] == 0:
        opcion = "w"
    
    elif jug[0] == 1:
        opcion = "a"
    elif jug[0] == 2:
        opcion = "s"
    elif jug[0] == 3:
        opcion = "d"


    
    #t.imprimir(matriz)
    
    print(opcion)
    matriz = t.mover(opcion, matriz)
    #time.sleep(0.02)
    #t.imprimir(matriz)
    gano = t.verificar(matriz)
    if gano:
        break

print(matriz)
print(mmm)
print("ganaste!")
