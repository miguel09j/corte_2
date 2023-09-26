from random import randint as r

def main(l):
    lista(l)
    m_n(l)

def lista(l):
    for i in range(10):
        l.append(r(1,50))
    print(l)
    return l
    
def m_n(l):
    l.sort()
    print(f"El numero menor de la lista es: {l[0]}")
    print(f"El numero mayor de la lista es: {l[-1]}")

if __name__ == "__main__":
    l = []
    main(l)