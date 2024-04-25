class Carro:
    def __init__(self, color, marca, modelo, combustible):
        self.color = color
        self.marca = marca
        self.combustible = combustible
        self.modelo = modelo

def LlenarDeposito(self):
    print(f"Recuerda llenar depósito del carro: {self.color}")

def ArrancarMotor(self):
    print(f"El carro {self.color} va a arrancar el motor")

def Frenar(self):
    print(f"El carro {self.marca} va a frenar" )

def Acelerar(self):
    print(f"El carro {self.color} va a acelerar")

def TocarClaxon(self):
    print(f"El carro {self.marca}va a tocar el claxon")


CarroVerde = Carro("Verde", "Honda", "HR-V", "Premium")
CarroAzul = Carro("Azul", "Audi", "A4", "Diesel")
CarroRojo = Carro("Rojo" , "Toyota", "Prius", "Eléctrico")


CarroAzul.ArrancarMotor()
CarroRojo.Frenar()