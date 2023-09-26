
def main_read1():
    f=open("matrizAsignacion (1).txt","rt")
    a=f.read()
    f.close()
    print(a)

def main_read2():
    f=open("matrizAsignacion (1).txt","rt")
    a = f.readline().rstrip("\n").split(",")
    while a != [""]:
        print(a)
        a = f.readline().rstrip("\n").split(",")
    f.close 


def suma(lista):
    for dato in lista:
        r = int(dato[0])+int(dato[1])+int(dato[3])
        salida+=str(r)+ ("\n")
    return r

def main_read3():
    f=open("matrizAsignacion (1).txt","rt")
    a = f.readlines()
    f.close
    lista = []
    for dato in a:
        lista.append(dato.rstrip("\n").split(","))
    print(lista)
    a = suma(lista)
    print(a)


if __name__=="__main__":
    main_read1()
    main_read2()
    main_read3()
    suma()