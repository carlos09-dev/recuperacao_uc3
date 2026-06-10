estacionamento = []

for i in range(2):
    linha = []
    for j in range(9):
        linha.append("Livre")
    estacionamento.append(linha)

opcao = 0

while opcao != 4:

    print("\n1 - Exibir vagas")
    print("2 - Cadastrar veículo")
    print("3 - Retirar veículo")
    print("4 - Sair")
    opcao = int(input("Escolha: "))

    if opcao == 1:
        for i in range(2):
            print(estacionamento[i])

    elif opcao == 2:
        placa = input("Digite a placa: ")
        lado = int(input("Lado (0 ou 1): "))
        vaga = int(input("Vaga (0 a 8): "))

        if estacionamento[lado][vaga] == "Livre":
            estacionamento[lado][vaga] = placa
            print("Veículo estacionado!")
        else:
            print("Vaga ocupada!")

    elif opcao == 3:
        placa = input("Digite a placa do veículo: ")

        encontrado = False

        for i in range(2):
            for j in range(9):
                if estacionamento[i][j] == placa:
                    estacionamento[i][j] = "Livre"
                    print("Veículo retirado da vaga:", i, j)
                    encontrado = True

        if encontrado == False:
            print("Placa não encontrada!")