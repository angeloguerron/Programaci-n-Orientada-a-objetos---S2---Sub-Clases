
from cuentas.cuenta import Cuenta

class CuentaAhorro(Cuenta):
    def aplicar_interes(self, tasa):
        self.saldo += self.saldo * tasa
