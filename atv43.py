velocidades = []

for i in range(6):
    velocidade = float(input("Digite a velocidade da volta: "))
    velocidades.append(velocidade)

print("Velocidades na ordem inversa:")

for i in range(5, -1, -1):
    print(velocidades[i])