# comando input()

# idade = input("quantos anos vc tem?")
# dessa forma vai dar erro, porque a resposta disso vai ser uma string. TYPE ERROR
# necessario converter para INTEIRO com int()
idade = int(input("quantos anos vc tem?"))
# ou tambem
# idade = int(idade)
print("exemplo de comando elif:")
if idade <=12:
    print("vc é criança")
    print("não pode tirar habilitação")
elif idade <=17:
    print("vc é adolescente")
    print("não pode tirar habilitação")
elif idade >= 18:
    print("vc é adulto")
    print("pode tirar habilitação")
else:
    print("idade nao suportada")