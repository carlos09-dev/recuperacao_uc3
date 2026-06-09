acima_190 = 0

for i in range(12):
    altura = float(input(f"Digite a altura do atleta {i+1}: "))

    if altura > 1.90:
        acima_190 += 1

print(f"\nQuantidade de atletas com mais de 1,90 m: {acima_190}")