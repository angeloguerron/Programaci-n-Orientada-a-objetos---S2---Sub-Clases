
from cuentas.cuenta_ahorro import CuentaAhorro
from cuentas.cuenta_corriente import CuentaCorriente

a = CuentaAhorro(1000)
a.aplicar_interes(0.1)

c = CuentaCorriente(500)
c.retirar(700)

print("Ahorro:", a.saldo)
print("Corriente:", c.saldo)
