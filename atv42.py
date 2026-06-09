dia = int(input("Informe o dia para pagamento (2, 5 ou 10): "))

while dia not in [2, 5, 10]:
    print("Dia inválido!")
    dia = int(input("Informe o dia para pagamento (2, 5 ou 10): "))

print("Boleto registrado.")