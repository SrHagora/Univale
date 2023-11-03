class Monitor:
    def __init__(self, marca, tamanho):
        self.marca = marca
        self.tamanho = tamanho

    def exibir_informacoes(self):
        print(f"Monitor {self.marca}, Tamanho: {self.tamanho} polegadas")


class Computador:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.monitor = None

    def conectar_monitor(self, monitor):
        if isinstance(monitor, Monitor):
            self.monitor = monitor
            print(f"Monitor {monitor.marca} conectado ao computador {self.marca} {self.modelo}")
        else:
            print("Erro: O objeto passado não é um monitor.")

    def exibir_informacoes(self):
        print(f"Computador {self.marca} {self.modelo}")
        if self.monitor:
            self.monitor.exibir_informacoes()
        else:
            print("Sem monitor conectado")

# Exemplo de uso:
monitor1 = Monitor("Dell", 24)
computador1 = Computador("HP","30")

computador1.exibir_informacoes()
monitor1.exibir_informacoes()

computador1.conectar_monitor(monitor1)
computador1.exibir_informacoes()
