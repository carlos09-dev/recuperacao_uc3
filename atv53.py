def gratificacao(salario):
    if mes >= 1 and mes <= 5:
        print("Gratificação: R$", salario * 0.30)

    elif mes >= 6 and mes <= 11:
        print("Gratificação: R$", salario * 0.40)

    elif mes == 12:
        print("Gratificação: R$", salario * 0.60)

salario = float(input("Digite o salário básico: "))
mes = int(input("Digite o mês (1 a 12): "))

gratificacao(salario)