n = int(input("Digite a quantidade de pilotos: "))

contador = 1
soma = 0

while contador <= n:
    nome = input("Nome do piloto: ")
    velocidade = float(input("Velocidade da volta: "))

    soma += velocidade

    if contador == 1:
        mais_rapido = nome
        maior_velocidade = velocidade

        mais_lento = nome
        menor_velocidade = velocidade
    else:
        if velocidade > maior_velocidade:
            maior_velocidade = velocidade
            mais_rapido = nome

        if velocidade < menor_velocidade:
            menor_velocidade = velocidade
            mais_lento = nome

    contador += 1

media = soma / n

print("Piloto mais rápido:", mais_rapido)
print("Piloto mais lento:", mais_lento)
print("Média das velocidades:", media)