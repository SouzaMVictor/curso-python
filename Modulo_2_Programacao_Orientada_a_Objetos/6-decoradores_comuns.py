# @classmethod
# @staticmethod


class MinhaClasse:
    # atributos de classe ficam fora do construtor
    # paramtros estaticos

    valor = 10 #atributo da classe; fora do construtor

    def __init__(self, nome) ->None:
        self.nome = nome #atributo da instancia

    # requer uma instncia para ser chamamdo
    def metodo_instancia(self):
        return f"metodo de instancia chamado para {self.nome}"


    # valor pode ser atribuido mesmo fora do construtor
    def segundo_metodo_instancia(self):
            return f"segundo metodo de instancia chamado para {self.valor}"

    @classmethod
    def metodo_classe(cls):
            # necessario passasr esse cls, como é no self que recebe a instancia 
            # cls recebe a classe
            # tem acesso aos attributos e metodos da classe
            return f"metodo da classe chamado para valor={cls.valor}"
    # não consigo pegar o nome, por exemplo

    @staticmethod
    # vai adicionar o comportamento de um metodo estatico
    # diferente do metodo da instancias e da class
    # nao recebe argumento
    # nao tem acesso aos atrigutos da classe nem da instancia
    # mas pode executar funcoes especificas

    def metodo_estatico():
        return "metodo estatico chamado"
         
obj = MinhaClasse(nome="classe exemplo")
print(obj.metodo_instancia())
#   metodo de instancia chamado para classe exemplo
print(obj.segundo_metodo_instancia())
#   segundo metodo de instancia chamado para 10

print(MinhaClasse.valor)
#   10
# também é possivel pq nao precisamos de instancia para acessar atributos da classe

print(MinhaClasse.metodo_classe())
#   metodo da classe chamado para valor=10
# acessamos diretamente pq usamos o classmethod

print(MinhaClasse.metodo_estatico())
    # metodo estatico chamado


# metodo de classe é usado para criar instancias a partir de configuracoes globais
class Carro:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    # metodo da classe Carro
    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(ano))


configuracao1= "toyota,corolla,2022"
carro1 =  Carro.criar_carro(configuracao1)
print(f"\nmarca: {carro1.marca}\n modelo: {carro1.modelo}\n ano: {carro1.ano}")



class Matematica:

    @staticmethod
    def somar(a,b):
        return a+b
print(Matematica.somar(a=12, b=15))
# 27
    