class Animal:
    def __init__(self, nome):
        self.nome = nome

    def mover(self):
        pass

class Cachorro(Animal):
    def mover(self):
        print(self.nome, 'correndo')

class Gato(Animal):
    def mover(self):
        print(self.nome, "andando")

cachorro = Cachorro("Rex")
gato = Gato('Preto')
cachorro.mover()
gato.mover()