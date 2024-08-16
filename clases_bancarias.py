class CuentaBancaria:

    interes_anual = 0.83 

    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, monto):
        if monto <= 0:
            print("El monto debe ser superior a 0.")
        else:
            print(f"Se depositaron ${monto} correctamente")
            self.saldo += monto
        
    def extraer(self, monto):
        if monto >= self.saldo:
            print(f"Saldo insuficiente...")
        else:
            self.saldo -= monto
            print(f"Ud. retiro ${monto}. Saldo actual: ${self.saldo}")

    @classmethod # Cuando se necesitan acceder o modificar atributos de clase
    def modificar_interes_anual(cls, interes):
        cls.interes_anual = round(interes, 2)
        
    def calcular_interes_diario(self):
        interes = round(self.interes_anual/365 * self.saldo, 2)
        self.saldo += interes
        print(f"Ud. gano {interes} de interes diario")

    @staticmethod # Cuando no se necesitan atributos de clase ni de instancia
    def calcular_monto_a_devolver(monto_solicitado, interes_anual, meses):
        print(f"Para {monto_solicitado} ustede debera devolver luego de {meses} meses: ${((1 + interes_anual * meses/12) * monto_solicitado):.2f}")

cuenta_1 = CuentaBancaria("Geronimo Franco")
cuenta_1.depositar(1000000)
cuenta_1.calcular_interes_diario()
CuentaBancaria.modificar_interes_anual(1.85)
cuenta_1.calcular_interes_diario()
cuenta_1.extraer(255000)
CuentaBancaria.calcular_monto_a_devolver(500000, 1.06, 36)

class Banco:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def ver_cuentas(self):
        print(self.cuentas)

    def ver_saldo(self):
        saldo = 0
        for cuenta in self.cuentas:
            saldo += cuenta.saldo 
        return saldo
