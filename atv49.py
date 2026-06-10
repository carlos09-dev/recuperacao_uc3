def vogal(letra):
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        return True
    else:
        return False

letra = input("Digite uma letra: ")

if vogal(letra):
    print("É vogal")
else:
    print("Não é vogal")