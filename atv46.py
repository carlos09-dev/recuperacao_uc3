# Programa para armazenar nome e gols de 11 jogadores

artilheiro = ""
maior_gols = 1

for i in range(11):
    nome = input(f"Digite o nome do {i+1}º jogador: ")
    gols = int(input(f"Digite a quantidade de gols de {nome}: "))

    if gols > maior_gols:
        maior_gols = gols
        artilheiro = nome

print("\n=== ARTILHEIRO DO TIME ===")
print("Nome:", artilheiro)
print("Quantidade de gols:", maior_gols)