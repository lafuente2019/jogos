import forca
import adivinhacao

print("*********************************")
print("******Escolha o seu jogo!********")
print("*********************************")

print("(1) Forca  (2) Adivinhação")

jogo = int(input("Qual jogo você quer jogar?"))

if(jogo == 1):
    print("******************************************")
    print("Bem vindo ao jogo de Forca")
    forca.jogar()
elif(jogo == 2):
    print("******************************************")
    print("Bem vindo ao jogo de adivinhação")
    adivinhacao.jogar()