import forca
import adivinhacao

count = 0
while(count == 0):
    print()
    print("*********************************")
    print("******Escolha o seu jogo!********")
    print("*********************************")
    print()

    print("(1) Forca  (2) Adivinhação  (0) Sair" )

    jogo = int(input("Qual jogo você quer jogar?"))
    print()


    if(jogo == 1):
        forca.jogar()
    elif(jogo == 2):
        adivinhacao.jogar()
    elif(jogo > 2):
        print("### Opção invalida ###")
    elif(jogo == 0):
        count +=1    
