import random


def jogar():
    
    imprime_welcome()
    numero_secreto = captura_numero_secreto()
    pontos = 1000
    nivel = nivel_jogo()

    total_de_tentativas = total_tentativas(nivel)

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue
        
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if(maior):
                print("O seu chute foi maior que o número secreto")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(
                        numero_secreto, pontos))


def imprime_welcome():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

def captura_numero_secreto():
    numero_secreto = random.randrange(1, 101)
    return numero_secreto

def nivel_jogo():
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))
    return nivel

def total_tentativas(nivel):
    if(nivel == 1):
        total_de_tentativas = 20
        return total_de_tentativas
    elif(nivel == 2):
        total_de_tentativas = 10
        return total_de_tentativas
    elif(nivel == 3):
        total_de_tentativas = 5
        return total_de_tentativas
        


if(__name__ == "__main__"):
    jogar()    


