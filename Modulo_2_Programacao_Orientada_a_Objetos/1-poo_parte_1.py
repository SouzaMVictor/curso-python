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