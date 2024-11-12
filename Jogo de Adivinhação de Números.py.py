# Criar um programa que desafia o usuário a adivinhar um número gerado 
# aleatoriamente pelo computador. 
import random
def main():
    numeroAleatorio = random.randint(1, 100)
    chances = 0
    max_chances = 10
    print("Vamos jogar? Bem-vindo ao game de advinhação numeral.")
    print("Então vamos começar,você precisa advinhar um número de 1 a 100")
    while chances < max_chances:
        chute = int(input("tenta a sorte ai, digite uma chance:"))
        if chute == numeroAleatorio:
            print("Que sorte! Você acertou!")
            break
        elif chute > numeroAleatorio:
            print("Vish errou, o número é menor.")
        else:
            print("Puts errou, seu número é maior.")
        chances += 1
    if max_chances == chances:
            print("Ihhhhh fim de jogo, errou tudo o número era", numeroAleatorio)

if __name__=='__main__':
    main()
