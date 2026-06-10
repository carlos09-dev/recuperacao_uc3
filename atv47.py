matriz = []
n = 1

for i in range(6):
    linha = []
    for j in range(7):
        linha.append(n)
        n += 1
    matriz.append(linha)

poltrona = int(input("Digite a poltrona desejada: "))

for i in range(6):
    for j in range(7):
        if matriz[i][j] == poltrona:
            matriz[i][j] = "X"

for i in range(6):
    print(matriz[i])