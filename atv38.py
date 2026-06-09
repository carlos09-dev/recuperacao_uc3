soma = 0
quantidade = 0

while soma < 100:
    numero = float(input("Digite um número: "))
    soma += numero
    quantidade += 1

print("Quantidade de números necessários:", quantidade)
print("Soma final:", soma)