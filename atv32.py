# Welcome to your Python project!


numeros = []
for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print(f"A soma de todos os números é: {sum(numeros)}")