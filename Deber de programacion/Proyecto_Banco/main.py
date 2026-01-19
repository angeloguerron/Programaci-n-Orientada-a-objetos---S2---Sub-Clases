#Implementa una clase base Cuenta para un sistema bancario, con métodos para depositar y retirar dinero. 
#Crea clases derivadas CuentaAhorro y CuentaCorriente con diferentes reglas para intereses y sobregiros.
from cuentas.cuenta_ahorro import CuentaAhorro
from cuentas.cuenta_corriente import CuentaCorriente
print("Bienvenido al sistema bancario")
a = CuentaAhorro(1000)
a.aplicar_interes(0.1)

c = CuentaCorriente(500)
c.retirar(700)

print("Ahorro:", a.saldo)
print("Corriente:", c.saldo)
