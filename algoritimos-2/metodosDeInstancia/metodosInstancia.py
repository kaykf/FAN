print('')
print('----------------------------------------------------')
print('Metodo Private')
print('----------------------------------------------------')
print('')
class Exemplo:
    def _init_(self):
        self.__numero_privado = 0

    def set_numero(self, numero):
        self.__numero_privado = numero

    def get_numero(self):
        return self.__numero_privado
    

exemplo = Exemplo()
exemplo.set_numero(42)
print(exemplo.get_numero())

print('')
print('----------------------------------------------------')
print('Exemplo - 01')
print('----------------------------------------------------')
print('')

'''
class Acesso:
    def _init_(self, email, senha):
        self.__senha = senha

user = Acesso('user@gmail.com', '12345678')

print(user.email)
print('')
'''

print('')
print('----------------------------------------------------')
print('Exemplo - 02')
print('----------------------------------------------------')
print('')

'''
class  Produto:
    imposto = 1.05
    contador = 0

    def _init_(self, nome, descricao, valor):
        self.id = Produto.contador = 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

    def desconto(self, porcentagem):
        return (self.__valor * (100 - porcentagem))/100


p1 = Produto('PlayStation5', 'Eletronico', 3500)
print(p1.desconto(10))
p2 = Produto('Geladeira Comsul', 'Eletrodomestico', 2000)
p3 = Produto('Maçã', 'Mercearia', 5,90)
p3.peso = '5kg'


print(p1.imposto)
print('')
print(p2.imposto)
print('')
print(p1.valor)
print('')
print(p2.valor)
'''
print('')
print('----------------------------------------------------')
print('Exemplo - 02')
print('----------------------------------------------------')
print('')

class Usuario:

    contador= 0

    @classmethod
    def n_usuarios(cls):
        print(f"Temos {cls.contador} usuários no sistema")

    def __init__(self,nome,sobrenome,email,senha):
        self.id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome= sobrenome
        self.__email = email
        self.__senha = senha
        Usuario.contador = self.id

    def nome_complete(self):
        return f"{self.__nome}{self.__sobrenome}"
    
user1 = Usuario('Paulo', 'Silva', 'Silva.paulo@python.com','12345')
user2 = Usuario('Lisa', 'Pereira', 'lis.pereira@python.com', '456789')
user3 = Usuario('Kayk', 'Felipe', 'kaykFelipe@python.com','1234')

print(user1.nome_complete())
print(user2.nome_complete())
print(user3.nome_complete())

Usuario.n_usuarios()