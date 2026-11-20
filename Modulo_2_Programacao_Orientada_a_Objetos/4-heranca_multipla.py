# classe herda multiplas subclasses

class Animal:
    def __init__(self, nome):
        self.nome = nome
    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando"

class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando"
# até aqui, exemplo deherança normal

class Morcego(Mamifero, Ave):
    # pega exemplos das duas classes mamiferos e ave
    def emitir_som(self):
    # super chama a implementacao da classe mae
    # porem a classe mae nao faz nada ainda
    # nao se usa dessa forma
        return super().emitir_som()


# acessando metodos da classe base "Animal"
morcego = Morcego(nome="Batman")
print("Nome do morcego:", morcego.nome)
print("Som do morcego:", morcego.emitir_som())

# acessando metodos da classe "Mamifero" e "Ave"
print("Morcego amamentando:", morcego.amamentar())
print("Morcego voando:", morcego.voar())