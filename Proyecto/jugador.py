import tablero as t
import numpy as np


matriz = t.generarMatriz2(3)


gano = False

while gano == False:
    t.imprimir(matriz)
    opcion = input("ingrese su movimiento (w,a,s,d) \n")
    matriz = t.mover(opcion, matriz)
    gano = t.verificar(matriz)

print(matriz)
print("ganaste!")
