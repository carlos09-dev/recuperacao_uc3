acertou = False

for tentativa in range(1, 6):
    numero = int(input("Digite a quantidade de bolinhas de gude: "))

    if numero == 82:
        print("Parabéns, você acertou!")
        acertou = True
        break
    elif numero < 82:
        print("Você errou! Existem mais bolinhas do que você digitou.")
    else:
        print("Você errou! Existem menos bolinhas do que você digitou.")

if not acertou:
    print("Suas 5 tentativas acabaram.")