from random import randint as r
import numpy as np

def main(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(r(1, 100))

        print(matriz[i])
    
    return matriz

def numeros_m_n(matriz):
    mayor = matriz[0][0]
    menor = matriz[0][0]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] < menor:
                menor = matriz[i][j]
            if matriz[i][j] > mayor:
                mayor = matriz[i][j]
    print("----------------------------------------------------------------------")
    print(f'El numero mayor de la matriz es: {mayor}')
    print(f'El numero menor de la matriz es: {menor}')
    print("-----------------------------------------------------------------------")

def matriz_o(matriz):
    matriz_o = np.sort(matriz, axis=None)
    print(f'La matriz ordenada de menor a mayor es:\n{matriz_o}')



if __name__ == "__main__":
    filas = 5
    columnas = 10
    matriz = main(filas, columnas)
    numeros_m_n(matriz)
    matriz_o(matriz)
