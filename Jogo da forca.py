import random

def main():
    def desenha_forca(chances):
        if chances == 5:
            print(" -----")
            print(" |   |")
            print("     |")
            print("     |")
            print("     |")
            print("     |")
            print("====|====")
        elif chances == 4:
            print(" -----")
            print(" |   |")
            print(" O   |")
            print("     |")
            print("     |")
            print("     |")
            print("====|====")
        elif chances == 3:
            print(" -----")
            print(" |   |")
            print(" O   |")
            print(" |   |")
            print("     |")
            print("     |")
            print("====|====")
        elif chances == 2:
            print(" -----")
            print(" |   |")
            print(" O   |")
            print("/|   |")
            print("     |")
            print("     |")
            print("====|====")
        elif chances == 1:
            print(" -----")
            print(" |   |")
            print(" O   |")
            print("/|\\  |")
            print("     |")
            print("     |")
            print("====|====")
        elif chances == 0:
            print(" -----")
            print(" |   |")
            print(" O   |")
            print("/|\\  |")
            print("/ \\  |")
            print("     |")
            print("====|====")

    palavras = ("python", "programacao", "desenvolvimento", "tecnologia")
    palavraSelecionada = random.choice(palavras)    
    chutes = []
    chances = 5
    ganhou = False

    while chances > 0 and not ganhou:
        
        palavra_oculta = ""
        for letra in palavraSelecionada:
            if letra in chutes:
                palavra_oculta += letra
            else:
                palavra_oculta += "_"
        
        print(f"A palavra é: {palavra_oculta}")
        
        if "_" not in palavra_oculta:
            ganhou = True
            print(f"Que sorte, você acertou. A palavra é: {palavraSelecionada}")
            break

        desenha_forca(chances)
        print(f"Você ainda tem {chances} chances.")
        
        tentativa = input("Tente a sorte, escolha uma letra: ").lower()
        
        if tentativa in chutes:
            print("Você já escolheu essa letra antes. Tente outra.")
        elif tentativa in palavraSelecionada:
            chutes.append(tentativa)
        else:
            chutes.append(tentativa)
            chances -= 1
            print(f"Que azar, você errou. A letra {tentativa} não está na palavra.")
    
    if not ganhou:
        desenha_forca(chances)
        print(f"Você perdeu! A palavra era: {palavraSelecionada}")
    else:
        print(f"Parabéns, você ganhou! A palavra era: {palavraSelecionada}")

if __name__ == "__main__":
    main()
