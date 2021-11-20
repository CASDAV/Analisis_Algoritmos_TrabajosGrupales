import tablero as t
import numpy as np


matriz = t.generarMatriz()


gano = False

while gano == False:
    for i in range(0,16):
        #sacar pos de 
        # 1) posicion actual de i
        # 2) posicion del numero a ubicar
        # 3) posicion del 0
        pass
    t.imprimir(matriz)
    opcion = input("ingrese su movimiento (w,a,s,d) \n")
    matriz = t.mover(opcion, matriz)
    gano = t.verificar(matriz)

print(matriz)
print("ganaste!")
