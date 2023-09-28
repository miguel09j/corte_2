class Personas():
    def __init__(self, nombre, peso, altura):
        self.nombre = nombre
        self.peso = peso
        self.altura = altura

    def indice(self):
        IMC = self.peso / ((self.altura / 100) ** 2)

        if IMC <= 18.5:
            return "por debajo"
        elif IMC <= 24.9:
            return "saludable"
        elif IMC <= 29.9:
            return "sobrepeso"
        elif IMC <= 34.9:
            return "obesidad I"
        elif IMC <= 39.9:
            return "obesidad II"
        else:
            return "obesidad III"


def main():
    estudiante1 = Personas("pedro", 97, 188)
    estudiante2 = Personas("maria", 47, 160)
    estudiante3 = Personas("julian", 58, 158)
    estudiante4 = Personas("jessica", 73, 170)

    print(f"Estudiante: {estudiante1.nombre}, resultado: {estudiante1.indice()}")
    print(f"Estudiante: {estudiante2.nombre}, resultado: {estudiante2.indice()}")
    print(f"Estudiante: {estudiante3.nombre}, resultado: {estudiante3.indice()}")
    print(f"Estudiante: {estudiante4.nombre}, resultado: {estudiante4.indice()}")


if __name__ == "__main__":
    main()
