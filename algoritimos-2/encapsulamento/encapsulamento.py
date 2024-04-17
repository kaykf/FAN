class contaBancaria:
    def __init__(self, titular, saldo=0):
        self.__titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar (self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print('Saldo Insuficiente.')

    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
conta = contaBancaria("João")
conta.depositar(100)
conta.sacar(50)
print("Saldo de", conta.get_titular(), ":", conta.get_)