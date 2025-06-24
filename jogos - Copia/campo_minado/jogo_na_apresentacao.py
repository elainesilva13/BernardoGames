def qualquer_coisa2():


    lista_de_cores=["amarelo","verde"]
    tentativas=3
    while tentativas:
        pergunta=input("Que cor eu estou pensando?   ").lower()
        if pergunta in lista_de_cores:
            print("você acertou!")
            break
        else:
            print("Você errou!")
            tentativas-=1
            print (tentativas)
    qualquer_coisa()

def qualquer_coisa():
    print("Qualquer coisa")

qualquer_coisa2()