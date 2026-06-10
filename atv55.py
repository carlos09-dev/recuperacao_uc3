def reajusta_gasolina(gasolina, reajuste):
    gasolina[0] = gasolina[0] + reajuste

def reajusta_etanol(etanol, gasolina, reajuste):
    etanol[0] = etanol[0] + reajuste
    gasolina[0] = gasolina[0] + (reajuste * 0.27)

gasolina = [float(input("Valor da gasolina: R$ "))]
etanol = [float(input("Valor do etanol: R$ "))]
reajuste = float(input("Valor do reajuste: R$ "))

combustivel = input("Combustível (G ou E): ")

if combustivel == "G":
    reajusta_gasolina(gasolina, reajuste)

elif combustivel == "E":
    reajusta_etanol(etanol, gasolina, reajuste)

print("Gasolina: R$", gasolina[0])
print("Etanol: R$", etanol[0])