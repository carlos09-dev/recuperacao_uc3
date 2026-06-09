maiores_que_50 = 0

for i in range(10):
    num = float(input(f"Digite o {i+1}º número: "))
    if num > 50:
        maiores_que_50 += 1

print(f"Quantidade de números maiores que 50: {maiores_que_50}")