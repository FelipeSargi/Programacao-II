class Computador:

    def __init__(self, marca, modelo, processador, memoriaram, hd):
        self.marca = marca
        self.modelo = modelo
        self.processador = processador
        self.memoriaram = memoriaram
        self.hd = hd
        self.monitor = None
    
    def conectar_monitor(self, monitor):
        if isinstance(monitor, Monitor):
            self.monitor = monitor
            return f"Monitor {monitor.marca} {monitor.modelo} está conectado ao computador {self.marca} {self.modelo}."
        else:
            return "Monitor INVALIDO."

class Monitor:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

computador1 = Computador("Chernobyll", "2.7", "Ryen 7 5000X", "64 GB", " 2TB")
monitor1 = Monitor("Samsung", "UltraWides")
print(computador1.conectar_monitor(monitor1))