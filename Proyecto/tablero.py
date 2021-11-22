import numpy as np
import random

def generarMatriz():
    matriz = np.empty((4, 4), dtype=int)
    matriz.fill(0)

    arr = []
    for i in range (0,16):
        arr.append(i)
    random.shuffle(arr)
    for i in range(0, 4):
        for j in range(0, 4):
            matriz[i][j] = arr[0]
            arr.pop(0)
    
    return matriz

def generarMatriz2():
    matriz = np.empty((4, 4), dtype=int)
    matriz.fill(0)

   
    cont = 1

    for i in range(0, 4):
        for j in range(0, 4):
            matriz[i][j] = cont
            cont +=1
    matriz[3][3] = 0
    return matriz

def generarMatriz3():
    matriz = np.empty((4, 4), dtype=int)
    matriz.fill(0)

   
    
    matriz[0] = [2,3,4,0]
    matriz[1] = [1,5,6,7]
    matriz[2] = [10,11,12,8]
    matriz[3] = [9,13,14,15]
    return matriz


def imprimir(matriz):
    print(matriz)


def verificar(matriz):
    ver1 = False
    ver2 = False
    cont = 1
    for i in range(0, 3):
        for j in range(0, 4):
            if matriz[i][j] == cont:
                ver1 = True
                cont += 1
            else:
                ver1 = False
                break
    if matriz[3][0] == 13 and matriz[3][1] == 14 and matriz[3][2] == 15 and matriz[3][3] == 0:
        ver2 = True
    else:
        ver2 = False
    if ver1 == True and ver2 == True:
        return True
    else:
        return False

def mover(opcion, m):
    
    pos = np.where(m == 0)
    x = pos[0][0]
    y = pos[1][0]
    #print(x,y)
    if opcion == "w":
        #mover arriba
        if x-1 >= 0:
            c1 = m[x][y]
            c2 = m[x-1][y]
            m[x-1][y] = c1
            m[x][y] = c2
        pass
    if opcion == "a":
        #mover iz
        if y-1 >= 0:
            c1 = m[x][y]
            c2 = m[x][y-1]
            m[x][y-1] = c1
            m[x][y] = c2
        pass
    if opcion == "s":
        #mover abajo
        if x+1 < 4:
            c1 = m[x][y]
            c2 = m[x+1][y]
            m[x+1][y] = c1
            m[x][y] = c2
        pass
    if opcion == "d":
        #mover derecha
        if y+1 < 4:
            c1 = m[x][y]
            c2 = m[x][y+1]
            m[x][y+1] = c1
            m[x][y] = c2
        pass
    return m
    