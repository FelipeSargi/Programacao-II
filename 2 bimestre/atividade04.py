class Cabeca:
    def __init__(self):
        self.estado = "Inteira"

    def destruir(self):
        self.estado = "Explodida"
        print("A cabeça foi EXPLODIDAA!")

class Boneco:
    def __init__(self):
        self.cabeca = Cabeca()

    def destruir(self):
        self.cabeca.destruir()
        print("O boneco está lascado!")

if __name__ == "__main__":
    boneco = Boneco()
    boneco.destruir()