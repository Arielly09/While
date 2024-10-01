import random

numero_secreto = random.randint(1, 10)
tentativa = 0 


while tentativa != numero_secreto:
    tentativa = int(input("Adivinhe um número entre 1 e 10: "))  # Solicita o palpite
    if tentativa < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif tentativa > numero_secreto:
        print("Muito alto! Tente novamente.")

print("Parabéns! Você acertou o número!")
