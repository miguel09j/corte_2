

class Pokemon():
    def __init__(self):
        self.color = None
        self.categoria = None
        self.tipo = None
        self.codigo = None


def main():
    pikachu = Pokemon()
    pikachu.color = "amarillo"
    pikachu.categoria = "raton"
    pikachu.tipo = "electrico"
    pikachu.codigo = 25
    print(id(pikachu))

    charizar = Pokemon()
    charizar.color = "naranja"
    charizar.categoria = "dragon"
    charizar.tipo = "fuego"
    charizar.codigo = 6
    print(id(charizar))

    ninetales = Pokemon()
    ninetales.color = "baige"
    ninetales.categoria = "zorro"
    ninetales.tipo = "fuego"
    ninetales.codigo = 38
    print(id(ninetales))

if __name__ == "__main__":
    main()