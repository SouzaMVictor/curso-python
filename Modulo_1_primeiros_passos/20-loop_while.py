# tipo de loop que repete um bloco de código enquanto uma condição for verdadeira

contador = 0

while contador < 5:
    # enquanto o contador for menor que 5
    print("contagem:", contador)
    # printa o contador 
    contador += 1
    # adiciona 1 ao acontador
    if contador ==  4:
        break
# finaliza quando chegar no resultado desejado
print("contador finalizado")
