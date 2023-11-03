class Cabeça:
    def __init__(self, tipo):
        self.tipo = tipo

    def descrever(self):
        print(f"Cabeça do tipo: {self.tipo}")


class Boneco:
    def __init__(self, nome, tipo_cabeça):
        self.nome = nome
        self.cabeça = Cabeça(tipo_cabeça)

    def descrever(self):
        print(f"Boneco: {self.nome}")
        self.cabeça.descrever()

    def destruir(self):
        print(f"O boneco {self.nome} foi destruído, incluindo sua cabeça.")
        del self


boneco1 = Boneco("Boneco 1", "Plástica")
boneco1.descrever()
boneco1.destruir()

