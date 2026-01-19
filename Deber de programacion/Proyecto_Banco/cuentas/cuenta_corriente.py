#Implementa una clase base Cuenta para un sistema bancario, con métodos para depositar y retirar dinero.
#Crea clases derivadas CuentaAhorro y CuentaCorriente con diferentes reglas para intereses y sobregiros.
from cuentas.cuenta import Cuenta

class CuentaCorriente(Cuenta):
    def retirar(self, monto):
        self.saldo -= monto
