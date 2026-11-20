# tipo especial de funcao que serve para modificar ou extender o comportamento de uma função/metodo sem alterar o codigo original da funcao

def meu_decorador(func):
    # func é o parametro
    # recebe a função que estou decorando
    # func() chama essa função
    def wrapper():
        # embrulho
        # vai envolta da função
        # fazer coisas depois e antes de ser chamado
        print("antes da função ser chamada")
        func()
        print("depois da função ser chamada")
    return wrapper
    # retorna sem chama-lo
    # retorna função como objeto. fica quadrada no nome minha_funcao, esperando ser chamada
@meu_decorador # @meu_decorador é um atalho para: minha_funcao = meu_decorador(minha_funcao)
def minha_funcao():
    # passada como argumento para meu_decorador. dentro dele, func passa a ser essa função.
    print("minha função foi chamada")


minha_funcao()
# está executando o wrapper e nao a função original 
# o decorador vai chamar a função
""" 
========explicação passo a passo ============== 
func é só um parâmetro, um nome qualquer (podia ser banana). Ele recebe a função que você está decorando, e func() chama essa função.
@meu_decorador
def minha_funcao():
    print("minha função foi chamada")

O @meu_decorador é um atalho para:
    minha_funcao = meu_decorador(minha_funcao)

o que acontece passo a passo:
1)minha_funcao (a função original) é passada como argumento para meu_decorador. Dentro dele, func passa a ser essa função original.
2)meu_decorador define o wrapper, que imprime algo, chama func() e imprime algo de novo.
3)meu_decorador devolve o wrapper (sem chamá-lo, por isso é return wrapper e não wrapper()).
4)O nome minha_funcao agora aponta para o wrapper, não mais para a função original.


Quando você faz minha_funcao(), na verdade está executando o wrapper, e é ele que chama o func() (a função original) no meio.

A diferença entre func e func()
func → a função em si, como objeto (você pode passar, guardar, devolver)
func() → executa a função

Por isso o decorador recebe func (sem parênteses) e só chama func() lá dentro do wrapper, no momento certo.

"""
# ============================================
# usado para validar se usuario ta logado
# decorador de autentificacao e adicionar antes das funcionalidades, vai verificar se está logado ou nao
# validações


# decorador como classes
class MeuDecoradroDeClasse:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self) -> Any:
        print("Antes da função ser chamada(classe)")
        self.func()
        print("Depois da função ser chamada(classe)")


@MeuDecoradroDeClasse
def segunda_funcao():
    print("chamando a segunda função")

segunda_funcao()