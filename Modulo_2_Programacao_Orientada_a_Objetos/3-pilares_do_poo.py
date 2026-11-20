# conceito usado em todas as linguagens orientadas a objetos

# exemplo de herança

print("\nexemplo de herança")

class Animal:
    def __init__(self,nome) -> None:
        self.nome = nome

        def andar(self):
            print(f"o animal {self.nome} andou")
            return
        def emitir_som(self):
            pass

# como exmeplo de herança, criar uma classe cachorro que herdará os métodos da classe mae dele, Animal.


class Cachorro(Animal):
    # exemplo de polimorfismo
    # usa os metodos da classe mae de outra forma
    def emitir_som(self):
        return "auau"

class Gato(Animal):
    def emitir_som(self):
        return "miau"



# variavel recebe a classe 
dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")


print("\nexemplo de polimorfismo")
animais = [dog, cat]
for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")


# encapsulamento

print("\nexemplo de encapsulamento")
# atributos privados para proteger dados
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo
        # dois underline antes do atributo = torna privado 

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo

conta = ContaBancaria(saldo=1000)
print(f"saldo da conta bancaria: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"saldo da conta bancaria: {conta.consultar_saldo()}")
conta.depositar(valor=-500)
print(f"saldo da conta bancaria: {conta.consultar_saldo()}")
conta.sacar(valor=200)
print(f"saldo da conta bancaria: {conta.consultar_saldo()}")

"""
    saldo da conta bancaria: 1000
    saldo da conta bancaria: 1500
    saldo da conta bancaria: 1500
    saldo da conta bancaria: 1300
"""

conta_do_zezinho = ContaBancaria(saldo=2000)

# abstração
#  criar um molde para construir uma classe
# protege caracteristicas e metodos de uma classe

print("exemplo de abstração")

from abc import ABC, abstractmethod
# modulo que permite criar classes base abstratas que definnem uma inteface para subclasses

class Veiculo(ABC):

    # @abstractmethod é um decorador
    # força as subclasses a implementarem o metodo ligar
    # senao nao vai ser possivel cria-la
    # é obrigado!!!
    @abstractmethod
    def ligar(self):
        pass
        # classes abstratas NÃO tem implementação

    @abstractmethod
    def desligar(self):
        pass


class Carro(Veiculo):
    def __init__(self) -> None:
        pass
    # def ligar(self):
    #     return "carro ligado"
    # vai dar erro pq precisa referenciar que vai usar os metodos descritos na classe Veiculo

    def ligar(self):
        return "carro ligado usando a chave"
    def desligar(self):
        return "carro desligado usando a chave"
# carro_amarelo = Carro()
    # essa implementação vai dar erro pq a classe Carro não tem os metodos obrigatorios para

carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())

# banco de dados => utilizar diretamente o bdd sem classe abstrata no meio = erro
# cria classe para acessar e precisa definir na classe abstrata os metodos que serão obrigatorios para acessar o banco de 
# tira complexidade da implementacao do banco de dados 
