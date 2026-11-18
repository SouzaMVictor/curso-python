#  o que é programação orientada a objetos?
    # adota conceitos especificos de linguagem orientada a objetos
    # organização de programas em torno de objetos
    # objetos: instancias de classes

# classes
    # plano que define e estrutura os objetos

class Pessoa:
    # descrever atributos e métodos
    def __init__(self, nome, idade) -> None:
        # construtor --> já tem essa estrutura padrão
        # função --> MÉTODO
        # self é a referencia a ele mesmo
            # rota de acesso
        # -> None --> metodo nao tem retorno
            # padrão de um construtor
        # na definição do objeto, é necessario escalar o uso da classe, entao nao usar atributos fixos
        self.nome = nome
        self.idade = idade
        pass
    def saudacao(self):
        return f"olá, meu nome é {self.nome} e eu tenho {self.idade} anos"
# objetos são instancias daquela classe
# podem representar o mundo real

pessoa1 = Pessoa("Victor", 26)
# o objeto tem que respeitar o que a classe demanda

# print(pessoa1.nome)
# print(pessoa1.idade)
"""
Victor
26
"""

mensagem = pessoa1.saudacao()
# cria-se uma variavel que conecta o objeto ao metodo

print(mensagem)
    # olá, meu nome é Victor e eu tenho 26 anos


# para criar outra pessoa usando o mesmo molde do primeiro

pessoa2 = Pessoa("Lê", 29)
mensagem  =pessoa2.saudacao()
print(mensagem)
# olá, meu nome é Lê e eu tenho 29 anos


# reutilização de código  grande vantagem da poo
# encapsulamento
# herança
# polimorfismo
    # serão discutidos em aulas seguintes


# desvantagens
    # complexidade
        # para programas simples beira o inviavel
            # desnecessario
    # curva de aprendizado ingrime
        # muita pratica
        # não é rápido
        