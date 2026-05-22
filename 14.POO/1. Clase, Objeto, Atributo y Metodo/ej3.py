class CuentaBancaria():
    def __init__(self,titular,saldo=0):
        self.titular=titular
        self.saldo=saldo
    def depositar(self,monto):
        self.saldo+=monto
        print(f"Deposito: S/{monto} -> saldo: S/.{self.saldo}")
    def retirar(self,monto):
        if self.saldo>=monto:
            self.saldo-=monto
            print(f"Retiro: S/{monto} -> saldo: S/.{self.saldo}")
        else:
            print("Saldo insuficiente.")
persona1=CuentaBancaria("Efrain",10000)
persona1.depositar(200)
persona1.retirar(8000)

