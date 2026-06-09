tentativas = 0
abaixo = 0
acima = 0

continuar = "S"

while continuar.upper() == "S":
    numero = int(input("Digite a quantidade de bolinhas de gude: "))
    tentativas += 1

    if numero == 82:
        print("Parabéns, você acertou!")
    elif numero < 82:
        print("Você errou! Existem mais bolinhas do que você digitou.")
        abaixo += 1
    else:
        print("Você errou! Existem menos bolinhas do que você digitou.")
        acima += 1

    continuar = input("Deseja continuar? (S/N): ")

print("\nRELATÓRIO FINAL")
print("Quantidade de tentativas:", tentativas)

if abaixo > acima:
    print("Erro mais comum: números abaixo de 82.")
elif acima > abaixo:
    print("Erro mais comum: números acima de 82.")
else:
    print("Houve a mesma quantidade de erros acima e abaixo de 82.")