senha = []
criptografada = ""

for i in range(6):
    letra = input("Digite uma vogal: ").lower()

    while letra not in ["a", "e", "i", "o", "u"]:
        letra = input("Inválido! Digite apenas vogais: ").lower()

    senha.append(letra)

for letra in senha:
    if letra == "a":
        criptografada += "z"
    elif letra == "e":
        criptografada += "3"
    elif letra == "i":
        criptografada += "I"
    elif letra == "o":
        criptografada += "0"
    elif letra == "u":
        criptografada += "$"

print("Senha digitada:", "".join(senha))
print("Senha criptografada:", criptografada)