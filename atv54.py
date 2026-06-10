def entrega3(valor):
    valor[0] = valor[0] + 25

def entrega5(valor):
    valor[0] = valor[0] + 20

def entrega7(valor):
    valor[0] = valor[0] + 15

def entrega10(valor):
    valor[0] = valor[0] + 10

valor = [float(input("Digite o valor da compra: "))]

print("1 - Entrega em 3 dias úteis")
print("2 - Entrega em 5 dias úteis")
print("3 - Entrega em 7 dias úteis")
print("4 - Entrega em 10 dias úteis")

opcao = int(input("Escolha a entrega: "))

if opcao == 1:
    entrega3(valor)
elif opcao == 2:
    entrega5(valor)
elif opcao == 3:
    entrega7(valor)
elif opcao == 4:
    entrega10(valor)
else:
    print("Opção inválida!")

print("Valor total: R$", valor[0])