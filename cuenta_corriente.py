
from cuentas.cuenta import Cuenta

class CuentaCorriente(Cuenta):
    def retirar(self, monto):
        self.saldo -= monto
