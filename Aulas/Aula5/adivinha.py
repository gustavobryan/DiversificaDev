import random

def jogar_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 0
    max_tentativas = 3

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 10.")
    print(f"Você tem {max_tentativas} tentativas.")

    while tentativas < max_tentativas:
        palpite = input("Digite seu palpite: ")

        if not palpite.isdigit():
            print("Por favor, insira um número válido.")
            continue

        palpite = int(palpite)
        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo!")
        elif palpite > numero_secreto:
            print("Muito alto!")
        else:
            print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
            break
    else:
        print(f"Suas tentativas acabaram. O número secreto era {numero_secreto}.")
        
jogar_adivinhacao()