soma = 0

for i in range(25):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))

    if i == 0:
        maior = nota
        menor = nota

    if nota > maior:
        maior = nota

    if nota < menor:
        menor = nota

    soma += nota

media = soma / 25

print(f"\nMaior nota: {maior}")
print(f"Menor nota: {menor}")
print(f"Média das notas: {media:.2f}"