
from random import randint as r

def main(filas,columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(r(1,10))

        print(matriz[i])
    #print(matriz)
    return matriz

def escalar(matriz):
    esc = int(input("ingrese el numero con el que quiere escalar la matriz: "))
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] *= esc
        print(matriz[i])

if __name__=="__main__":
    filas = int(input("ingrese el numero de filas: "))
    columnas = int(input("ingrese el numero de columnas: "))
    print("---original--------")
    matriz=main(filas,columnas)
    print("-------escalada-----")
    escalar(matriz)