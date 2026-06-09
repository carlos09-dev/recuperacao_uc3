soma = 0
quantidade = 0

while soma < 100:
    numero = float(input("Digite um número maior que 0: "))

    while numero <= 0:
        print("Número inválido!")
        numero = float(input("Digite um número maior que 0: "))

    soma += numero
    quantidade += 1

print("Quantidade de números necessários:", quantidade)