def selec_producto():
    f=open("Alimentos.txt","rt")
    a = f.readlines()
    f.close
    lista = []
    for dato in a:
        lista.append(dato.rstrip("\n").split(","))
    print(lista)

def selec_alimento():
    lista_p = []

    with open('Alimentos.txt', 'r') as f:
        lineas = f.readlines()
        for line in lineas:
            parts = line.strip().split(',')
            lista_p.append(parts[1].lower())

    while True:
        producto = input("Ingrese el nombre del producto que compró o escriba 'salir' para terminar:\n").lower()

        if producto == 'salir':
            break

        if producto in lista_p:
            precio_p = float(input(f"Ingrese el valor que le cobraron por el producto '{producto}':\n"))
            indice = lista_p.index(producto)
            iva = float(lineas[indice].split(',')[2])
            sin_iva = precio_p / (1 + iva)
            valor_iva = precio_p - sin_iva
            print(f'El costo del alimento {producto} es: {sin_iva}')
            print(f'El valor del IVA es: {valor_iva}')
        else:
            print('El alimento ingresado no está en el menú o catálogo de alimentos.')

 
if __name__ == '__main__':
    selec_producto()
    metodo()
